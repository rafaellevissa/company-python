import os
from dotenv import load_dotenv

dotenv_paths = ['/run/secrets/company-python', os.path.realpath(os.getcwd() + "/.env")]

for dotenv_path in dotenv_paths:
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

appkey = os.getenv("APP_KEY")

dbdrive = os.getenv("DB_DRIVE")
dbuser = os.getenv("DB_USER")
dbpassword = os.getenv("DB_PASSWORD")
dbhost = os.getenv("DB_HOSTNAME")
dbport = os.getenv("DB_PORT")
dbname = os.getenv("DB_DATABASE")
