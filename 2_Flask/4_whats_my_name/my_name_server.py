from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
  print "Got Post Info"
  name = request.form['name']
  print request.form
  return redirect('/')

# @app.route('/name')
# def name():
#     return render_template('name.html')

app.run(debug=True)
