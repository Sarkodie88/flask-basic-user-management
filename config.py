import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
db = os.environ.get("DB")

print("host is: ", host)

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(username, password, host, db)
SQLALCHEMY_TRACK_MODIFICATIONS = "True"

SECRET_KEY = os.environ.get("SECRET_KEY")

