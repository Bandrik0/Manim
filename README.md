🎬 Manim Logo Renderer WebApp

A simple web application to create animated logo videos using Manim.Upload your logo (SVG or PNG) → choose an animation style → instantly get a rendered MP4 video.

✨ Features

Multiple Animation Styles:

Draw (outline tracing)

Fade In

Bounce

Supports SVG and PNG logos

Rendered with Manim for smooth vector animations

Docker-ready → Deploy on Hugging Face Spaces for free

FastAPI backend + simple HTML/JS frontend

📂 Project Structure

MANIM-LOGO-WEBAPP
│
├── backend
│   ├── app.py              # FastAPI server
│   ├── renderer.py         # Manim rendering logic
│   ├── requirements.txt    # Backend dependencies
│
├── frontend
│   ├── index.html          # Web UI for uploading and selecting animations
│
├── Dockerfile              # Hugging Face Spaces Docker setup
├── .gitignore
└── README.md

🚀 Local Setup

1. Clone the repo

git clone https://github.com/<your-username>/manim-logo-webapp.git
cd manim-logo-webapp

2. Create a virtual environment & install dependencies

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r backend/requirements.txt

3. Run the backend server

uvicorn app:app --app-dir backend --host 127.0.0.1 --port 8000 --reload

The backend will be available at:http://127.0.0.1:8000

🌐 Deploy to Hugging Face Spaces

Create a new Docker Space on Hugging Face Spaces.

Upload all project files, keeping the folder structure.

The included Dockerfile will handle dependencies and start the FastAPI server.

Once built, your app will be available at:

https://<username>-<space-name>.hf.space/web

🛠 Dependencies

Python 3.10+

Manim

FastAPI

Uvicorn

ffmpeg (required by Manim)

📜 License

MIT License — feel free to modify and use.

❤️ Credits

Built with Manim & FastAPI.Inspired by creative coding & animation projects.

