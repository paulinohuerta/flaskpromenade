from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/catalog_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

admin = Admin(app)

import my_app.catalog.views as views
admin.add_view(views.HelloView(name='Hola'))

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

admin.add_view(ModelView(views.Category,db.session))
admin.add_view(ModelView(views.Product,db.session))

