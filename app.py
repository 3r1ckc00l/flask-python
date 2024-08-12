from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data')
def getdata():
    data = ['IF-4201','IF-4202','IF-4203']
    return render_template('index.html', data=data)

@app.route('/name/<string:name>')
def getname(name):
    return "Your name is {}".format(name)

if __name__ == "__main__":
    app.run(debug=True)
