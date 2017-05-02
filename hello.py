from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/person/<name>')
def person(name):
    return render_template('person.html',a_name=name)

if __name__ == '__main__':
    app.run(port=5003,debug=True)

