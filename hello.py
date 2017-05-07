from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/person/<name>')
def user(name):
    return render_template('person.html', name=name)

if __name__ == '__main__':
    app.run(port=5003,debug=True)

