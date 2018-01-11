from my_app import db

class User(db.Model):
    #__tablename__ = 'user_db'
    username = db.Column(db.String(15),primary_key=True)
    password = db.Column(db.String(12))
    dni = db.Column(db.String(9))
    nombre = db.Column(db.String(20))
    apellidos = db.Column(db.String(40))
    edad = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username


