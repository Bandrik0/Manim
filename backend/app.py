\
import os
import uuid
import shutil
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from renderer import render_logo

app = FastAPI(title="Manim Logo Renderer")

# Allow local dev frontends; tighten in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "/tmp/logo_uploads"
RENDER_DIR = "/tmp/logo_renders"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RENDER_DIR, exist_ok=True)

VALID_ANIMS = {"draw", "fade", "spin", "bounce"}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/render")
async def render(
    file: UploadFile = File(...),
    animation: str = Form("draw"),
    duration: float = Form(4.0),
    bg_color: str = Form("#111111"),
    quality: str = Form("m"),  # l,m,h,u
):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in {".svg", ".png", ".jpg", ".jpeg", ".webp"}:
        raise HTTPException(status_code=400, detail="Bitte SVG/PNG/JPG/WEBP hochladen.")

    if animation not in VALID_ANIMS:
        raise HTTPException(status_code=400, detail=f"Unknown animation: {animation}")

    # Save upload
    uid = str(uuid.uuid4())
    upload_path = os.path.join(UPLOAD_DIR, f"{uid}{ext}")
    with open(upload_path, "wb") as out:
        shutil.copyfileobj(file.file, out)

    # Render output
    out_path = os.path.join(RENDER_DIR, f"{uid}.mp4")
    try:
        render_logo(
            input_path=upload_path,
            output_path=out_path,
            animation=animation,
            duration=float(duration),
            bg_color=bg_color,
            quality=quality,
        )
    except Exception as e:
        # surface manim errors
        return JSONResponse(status_code=500, content={"error": str(e)})

    return FileResponse(out_path, media_type="video/mp4", filename="logo_animation.mp4")
