# 🎬 Manim Logo Renderer WebApp

Create beautiful animated logo videos in seconds using [Manim](https://www.manim.community/)!  
Upload your logo (SVG/PNG), pick an animation, and download your MP4 — all in your browser.

---

## ✨ Features
- **Multiple Animations:** `draw` (SVG outline tracing), `fade`, `spin`, `bounce`
- **Customizable:** Set background color, animation duration, and video quality
- **Instant Preview:** Drag & drop logo, see animation options, download result
- **Simple Stack:** FastAPI backend (Python), minimal HTML/JS frontend
- **Docker-ready:** 1-click deploy to **Hugging Face Spaces** or run locally

---

## 📂 Project Structure
```
.
├── backend/
│   ├── app.py            # FastAPI app: POST /render, GET /health, serves /web
│   ├── renderer.py       # Manim scene generator + CLI render
│   ├── requirements.txt  # Python dependencies for backend + Manim
├── frontend/
│   └── index.html        # Drag & drop UI
├── Dockerfile            # Root-level, for Hugging Face Spaces & Docker
├── .gitignore
└── README.md
```

---

## 🚀 Local Setup

**Requirements:**  
- Python 3.11+  
- `ffmpeg` (if not using Docker)  
- On Apple Silicon (macOS M1/M2), Manim is easiest via conda-forge (see Troubleshooting below)

### 1. Create a virtual environment & install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r backend/requirements.txt
```

### 2. Run the backend server
```bash
uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8000 --reload
```

### 3. Open the web UI
Just open `frontend/index.html` in your browser.

Health check: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health) → returns `{"ok": true}`

---

## 🐳 Deploy on Hugging Face Spaces (or Docker)

1. **On Hugging Face Spaces:**  
   - Click "Create Space", choose **Docker** as the SDK, and point to this repo.
   - The included `Dockerfile` handles all dependencies.

2. **With Docker locally:**  
   ```bash
   docker build -t manim-logo-webapp .
   docker run -p 8000:8000 manim-logo-webapp
   ```
   Then open `frontend/index.html` and use as above.

---

## 🛠️ Troubleshooting / Notes
- **Apple Silicon (M1/M2):**  
  Manim works best via conda.  
  ```bash
  brew install miniforge
  conda create -n manim python=3.11
  conda activate manim
  pip install -r backend/requirements.txt
  ```
- **SVGs:** For best results, use simple SVG logos (single path or group).
- **Security:** The backend does not persist uploads or output files.

---

## 📦 Dependencies
- [Manim Community Edition](https://www.manim.community/) (video rendering)
- [FastAPI](https://fastapi.tiangolo.com/) (API backend)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- [Pillow](https://python-pillow.org/) (image processing)
- [ffmpeg](https://ffmpeg.org/) (video encoding, must be installed system-wide)

All backend Python dependencies are listed in `backend/requirements.txt`.

---

## 📝 License

Free to Use

---

## 🙏 Credits

- Built by [@beitkhalaf](https://github.com/beitkhalaf)
- Powered by [Manim Community](https://www.manim.community/)
- Inspired by open-source creativity!
