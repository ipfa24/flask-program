from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey There '+'Imron Mustari'

@app.route('/about')
def about():
    return '51421667_2IA02'

@app.route('/university')
def about():
    return 'Gunadarma_University'

if __name__ == '__main__':
    app.run()
