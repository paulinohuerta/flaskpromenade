from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/catalog_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

api = Api(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()

