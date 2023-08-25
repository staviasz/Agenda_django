from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
static_path = str(BASE_DIR / "static")

workers = 4
bind = "127.0.0.1:8001"
static_url = "/static/"
