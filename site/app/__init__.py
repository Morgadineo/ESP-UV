# app/__init__.py
from flask            import Flask
from config           import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate

app = Flask(__name__)           # Instância do app flask
app.config.from_object(Config)  
db      = SQLAlchemy(app)       # Instância do banco de dados
migrate = Migrate(app, db)      # Instância de migração

from app import routes, models
