from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.environ.get("POSTGRES_DB")

DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")

DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")


APP_ADDRESS = os.environ.get("APP_ADDRESS")
APP_PORT = os.environ.get("APP_PORT")

TASKS_API_URL = os.environ.get("TASKS_API_URL")


