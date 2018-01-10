from flask import request, Blueprint
from my_app import app, db
from flask_admin import BaseView, expose
from my_app.catalog.models import Category, Product

catalog = Blueprint('catalog', __name__)

class HelloView(BaseView):
   @expose('/')
   def index(self):
     return self.render('some-template.html')
