import os
import subprocess
import tempfile
from pathlib import Path


def _scene_code(input_path: str, animation: str, duration: float, bg_color: str) -> str:
    is_svg = str(input_path).lower().endswith(".svg")
    return f"""
from manim import *
from manim import rate_functions as rf

class LogoScene(Scene):
    def construct(self):
        config.background_color = "{bg_color}"
        path = r{input_path!r}
        is_svg = {str(is_svg)}

        if is_svg:
            try:
                mobj = SVGMobject(path)
                mobj.set_height(5).move_to(ORIGIN)

                if {animation!r} == "draw":
                    # Fill'leri kapat, stroke'u görünür yap
                    for sm in mobj.family_members_with_points():
                        if hasattr(sm, "set_fill"):
                            sm.set_fill(opacity=0)
                        if hasattr(sm, "set_stroke"):
                            sm.set_stroke((sm.stroke_color or WHITE),
                                          width=(sm.stroke_width or 2),
                                          opacity=1.0)

                    parts = [sm for sm in mobj.family_members_with_points() if sm.has_points()]
                    if len(parts) == 0:
                        self.add(mobj)
                        self.play(FadeIn(mobj, run_time={duration}))
                        self.wait(0.2)
                        return

                    self.play(
                        LaggedStart(*[Create(p) for p in parts], lag_ratio=0.05),
                        run_time=max(0.6, {duration}*0.85)
                    )
                    # fill'leri geri getir
                    self.play(
                        *[p.animate.set_fill(opacity=1.0) for p in parts if hasattr(p, "set_fill")],
                        run_time=max(0.2, {duration}*0.15)
                    )
                    self.wait(0.2)
                    return
            except Exception:
                is_svg = False

        # SVG değilse (veya draw değilse) fallback
        if not is_svg:
            mobj = ImageMobject(path).set_height(5).move_to(ORIGIN)

        if {animation!r} == "spin":
            self.play(FadeIn(mobj, run_time=max(0.2, {duration}*0.25), scale=0.8))
            self.play(Rotate(mobj, angle=TAU, run_time=max(0.4, {duration}*0.75)))
            self.wait(0.2)
        elif {animation!r} == "bounce":
            # küçük başlat → orijinal boyuta "zıplayarak" gel
            mobj.scale(0.01)
            self.add(mobj)
            self.play(
                mobj.animate.scale(100),
                run_time=max(0.4, {duration}*0.6),
                rate_func=rf.ease_out_back
            )
            self.play(
                mobj.animate.scale(0.95),
                run_time=max(0.2, {duration}*0.2),
                rate_func=rf.ease_out_sine
            )
            self.wait(0.2)
        else:
            # fade
            self.play(FadeIn(mobj, run_time={duration}))
            self.wait(0.3)
"""


def render_logo(input_path: str, output_path: str, animation: str, duration: float, bg_color: str, quality: str = "m"):
    qflag = {"l": "-ql", "m": "-qm", "h": "-qh", "u": "-qu"}.get(quality.lower(), "-qm")

    with tempfile.TemporaryDirectory() as tmpdir:
        scene_file = Path(tmpdir) / "logo_scene.py"
        scene_file.write_text(_scene_code(str(input_path), animation, duration, bg_color), encoding="utf-8")

        cmd = [
            "manim",
            qflag,
            str(scene_file),
            "LogoScene",
            "-o", "logo_render.mp4",
            "--format", "mp4",
            "--disable_caching",
            "--media_dir", tmpdir,
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Manim failed: {e.stderr or e.stdout}")

        vid = None
        for p in Path(tmpdir).rglob("*.mp4"):
            if p.name.endswith(".mp4"):
                vid = p
                break
        if not vid:
            raise RuntimeError("Render output not found.")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(vid, "rb") as src, open(output_path, "wb") as dst:
            dst.write(src.read())
