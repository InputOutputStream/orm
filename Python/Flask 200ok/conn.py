from flask_sqlalchemy import SQLAlchemy


db_name  ='test'
user = 'hge'
pswd = "hge"
host = "localhost"

con_url = f'postgresql://{user}:{pswd}@{host}/{db_name}'

db = SQLAlchemy()
