from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hallo Im'+'Imron Mustari'

@app.route('/about')
def about():
    return '51421667_2IA02'

if __name__ == '__main__':
    app.run()
