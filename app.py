from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from mockdbhelper import MockDBHelper as DBHelper
from user import User
from flask import redirect, url_for, request

app = Flask(__name__)
login_manager = LoginManager(app)
DB = DBHelper()
app.secret_key = 'lWV6+txk+19MCmhl40BDYhvKk/DEu8FtzmLauU0y'

@app.route("/")
def home():
  #return "Under construction"
  return render_template("home.html")

@app.route("/account")
@login_required
def account():
  return "You are logged in"

@app.route("/login", methods=["POST"])
def login():
  email = request.form.get("email")
  password = request.form.get("password")
  user_password = DB.get_user(email)
  if user_password and user_password == password:
     user = User(email)
     login_user(user)
     return redirect(url_for('account'))
  return home()

@login_manager.user_loader
def load_user(user_id):
  user_password = DB.get_user(user_id)
  if user_password:
    return User(user_id)

if __name__ == '__main__':
  app.run(port=5300, debug=True)
