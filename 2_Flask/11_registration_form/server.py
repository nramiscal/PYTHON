from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank")
    # elif not NAME_REGEX.match(request.form['first_name']):
    #     flash("First name cannot contain numbers")
    elif hasNumbers(request.form['first_name']) == True:
        flash("First name cannot contain numbers")
    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank")
    # elif not NAME.match(request.form['last_name']):
    #     flash("Last name cannot contain numbers")
    elif hasNumbers(request.form['last_name']) == True:
        flash("Last name cannot contain numbers")
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    if len(request.form['password']) < 1:
        flash("Password cannot be black")
    elif len(request.form['password']) > 8:
        flash("Password cannot exceed 8 characters")
    if len(request.form['pass2']) < 1:
        flash("Password confirmation cannot be blank")
    elif request.form['password'] != request.form['pass2']:
        flash("Passwords do not match")
    else:
        flash("Thanks for submitting your information.")
    return redirect('/')

app.run(debug=True)
