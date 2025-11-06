"""Provide global constants for the API server."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
API_DATA_DIR = Path("data")
API_DATA_PATH = (PROJECT_ROOT / API_DATA_DIR).resolve()
# blog storage
BLOG_FILE = Path("blog.json")
BLOG_FILE_PATH = (API_DATA_PATH / BLOG_FILE).resolve()
# sequence storage
SEQUENCE_FILE = Path("sequence.json")
SEQUENCE_FILE_PATH = (API_DATA_PATH / SEQUENCE_FILE).resolve()