from flask import Flask, request, render_template
app = Flask(__name__)

app.secret_key = "hideme"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    print red
    print green
    print blue
    return render_template('index.html', red=red, green=green, blue=blue)

app.run(debug=True)
