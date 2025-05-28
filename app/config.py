import os
from dotenv import load_dotenv

load_dotenv()


DOMEN = "127.0.0.1:8000"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/auth_db")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60