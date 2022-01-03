from dotenv import load_dotenv
import os

load_dotenv()

# Database setup production
db_user = os.getenv('DB_USERNAME')
db_url = os.getenv('DB_URL')
db_name = os.getenv('DB_NAME')
db_password = os.getenv('DB_PASSWORD')

SQLALCHEMY_DATABASE_URI= f'postgresql://{db_user}:{db_password}@{db_url}:5432/{db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
