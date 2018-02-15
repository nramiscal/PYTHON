from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    print 'counter = ' + str(session['counter'])
    return render_template('index.html', count = session['counter'])

@app.route('/add2')
def add2():
    session['counter'] += 2
    return render_template('index.html', count = session['counter'])

@app.route('/reset')
def reset():
    session['counter'] = 1
    return render_template('index.html', count = session['counter'])

app.run(debug=True)
