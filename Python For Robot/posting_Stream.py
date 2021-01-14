print('Hello')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   ret_things = "Hello World in Flask World !!!"
   return ret_things

@app.route('/next')
def next():
    a="11"
    return a
if __name__ == '__main__':
   app.run()