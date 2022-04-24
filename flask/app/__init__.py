from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy()
app = Flask(__name__)

db.init_app(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@localhost:5433/test"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/test"  # 本機端Postgres資料庫測試用

from .blueprints.example import api_page as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/example')