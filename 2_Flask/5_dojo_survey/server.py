from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    print "Got Post Info"
    for key in request.form:
        session[key] = request.form[key]
    print request.form
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

app.run(debug=True)
    