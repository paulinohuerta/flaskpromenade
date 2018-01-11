from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.user.models import User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.context_processor
def some_processor():
    def full_name(user):
        return '{0} / {1} / dni [{2}] / edad: {3}'.format(user.nombre, user.apellidos, user.dni, user.edad)
    return {'full_name': full_name}


@user_blueprint.route('/')
@user_blueprint.route('/home')
def home():
    return render_template('home.html', users=User.query.all())

@user_blueprint.route('/user/<key>')
def user(key):
    user = User.query.filter(User.username == key).first()
    if not user:
        abort(404)
    return render_template('user.html', user=user)
