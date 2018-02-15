from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    query = "SELECT email FROM users"
    session['email_str'] = ""
    emails = mysql.query_db(query)
    session['email_str'] += str(emails)
    # print email_str
    return render_template('index.html')

@app.route('/check', methods = ['POST'])
def check():
    session['email'] = request.form['email']
    if session['email_str'].find(session['email']) == -1:
        flash("Not a valid email")
        return redirect('/')
    else:
        # flash("Success! There is a match")
        # return redirect('/')
        return redirect('/success')


@app.route('/success', methods = ['GET'])
def show():
    query = "SELECT email, created_at FROM users"
    show_emails = mysql.query_db(query)
    print show_emails
    return render_template('success.html', show_emails=show_emails)





app.run(debug=True)
