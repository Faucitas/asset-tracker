# Database setup development
user = 'postgres'
db_url = 'localhost:5432'
db_name = 'asset_tracker'


SQLALCHEMY_DATABASE_URI= f'postgresql://{user}@{db_url}/{db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False