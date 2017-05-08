from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'spring_bank_app_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/create',methods=['POST'])
def create():
    return render_template('create.html')

@app.route('/view1',methods=['POST'])
def view1():
    deposit = request.form['depositAmount']
    tenure = request.form['tenure']
    return render_template('view1.html',a_tenure=tenure,a_deposit=deposit)

@app.route('/index')
def main():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from fixed_deposit_details")
    data = cursor.fetchone()
    ar1=[]
    while data is not None:
      ar1.append(data)  
      data = cursor.fetchone()
    return render_template('index.html',bb=ar1)

if __name__ == '__main__':
    app.run(port=5003,debug=True)



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5003,debug=True)

