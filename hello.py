from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/person/<name>')
def person(name):
    return render_template('person.html',a_name=name)

@app.route('/advices')
def advices():
    data = [
       'Always finish what you started',
       'Do what you\'re doing your best',
       'Do not cling to anything that will eventually destroy you'
    ]
    return render_template('advices.html', comments=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug=True)

