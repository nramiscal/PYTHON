from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods = ['POST'])
def process():
    for key in request.form:
        session[key] = request.form[key]
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Comment cannot exceed 120 characters")
        return redirect('/')
    else:
        return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

app.run(debug=True)
