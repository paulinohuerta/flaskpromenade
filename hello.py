from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    # I am interested in using the port 5003, if it does not indicate
    # the 5000 takes by default.
    # debug enabled means activate debugger and reloader.
    app.run(port=5003,debug=True)

