"""Configuration options."""

from pathlib import Path

ROOT_DIR = Path(__file__).parents[1]
UPLOADS_DIR = ROOT_DIR / 'dynamic' / 'UPLOADS'
EXPORTS_DIR = ROOT_DIR / 'dynamic' / 'EXPORTS'

IMAGE_CONVERSION_MODE = 'RGB'

UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
