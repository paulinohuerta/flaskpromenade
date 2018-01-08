from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/usuarios_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(15),primary_key=True)
    password = db.Column(db.String(12))
    dni = db.Column(db.String(9))
    nombre = db.Column(db.String(20))
    apellidos = db.Column(db.String(40))
    edad = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
 list1 = User.query.all() 
 us1 = list1[0]
 st2 = '<h3>' + us1.nombre + ' has a username <i>' + us1.username + '</i></h3>'
 st = ''
 for u in list1:
   st = st + '<h1>' + u.username + ' -- <i>' + u.dni + '</i> -- ' + '</h1>'
 return st2 + st

