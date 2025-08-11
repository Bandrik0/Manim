# Manim Logo Renderer (FastAPI + Frontend)

**Logo yükle → animasyon seç → MP4 al.**  
SVG için “draw” (çizme) animasyonu, PNG/JPG için fade/spin/bounce.

<p align="center">
  <img alt="demo" src="https://img.shields.io/badge/FastAPI-0.111.0-009688?logo=fastapi">
  <img alt="demo" src="https://img.shields.io/badge/Manim-0.19.0-6E4C13">
  <img alt="demo" src="https://img.shields.io/badge/Docker-ready-0db7ed?logo=docker">
</p>

## Özellikler
- **/web**: Basit web arayüzü (drag & drop).
- **POST /render**: FastAPI endpoint’i MP4 döner.
- Animasyonlar: `draw` (SVG), `fade`, `spin`, `bounce`.
- Arka plan rengi, süre ve kalite seçimi.

## Dizin Yapısı
.
├─ backend/
│ ├─ app.py # FastAPI, /render + /web
│ ├─ renderer.py # Manim çağrısı + sahne üretimi
│ ├─ requirements.txt # Python bağımlılıkları
├─ frontend/
│ └─ index.html # Minimal UI
├─ Dockerfile # (root) Hugging Face Spaces / Docker deploy
└─ README.md


---

## Lokal Çalıştırma (Mac/Linux/Windows)
> Python 3.11+, ffmpeg gerekir (Docker kullanırsan gerekmez).

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8000 --reload
