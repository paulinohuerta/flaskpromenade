from flask import Flask, render_template
import redis

app = Flask(__name__)

@app.route('/index')
def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    the_set = r.get('nameSet')
    members_set=[]
    members_set = r.smembers(the_set) 
    return render_template('index.html',var=the_set,listA=members_set)

if __name__ == '__main__':
    app.run(port=5003,debug=True)

