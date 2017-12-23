from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/person/<a_name>')
def person(a_name):
    return '<h1>Hello, %s</h1>' % a_name

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return '<h1>Hello, %s </h1><h3>password=%s</h3>' % (username, password)

@app.route('/person/<a_name>/edad/<int:age>')
def theage(a_name,age):
    rest = 100 - age
    return '<h1>Hello, %s </h1><h3>In %d years you will have one hundred years</h3>' % (a_name, rest)

if __name__ == '__main__':
    app.run(port=5003,debug=True)

