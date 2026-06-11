import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DB_NAME = os.getenv("SUPABASE_DATABASE")
DB_HOST = os.getenv("SUPABASE_HOST")
DB_PORT = os.getenv("SUPABASE_PORT")
DB_USER = os.getenv("SUPABASE_USER")
DB_PASSWORD = os.getenv("SUPABASE_PWD")
DB_ANON = os.getenv("SUPABASE_ANON")
DB_JWT = os.getenv("SUPABASE_JWT")