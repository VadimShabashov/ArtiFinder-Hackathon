import os
from dotenv import load_dotenv

load_dotenv() 

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASS = os.getenv("DATABASE_PASS")