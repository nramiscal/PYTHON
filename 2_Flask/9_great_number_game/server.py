from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='ThisIsSecret'




@app.route('/')
def index():
    session['number'] = random.randrange(0, 101) # random number between 0-100
    print 'The correct number is ' + str(session['number'])
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    num = request.form['number']
    print 'Num is ' + num
    print 'The correct number is ' + str(session['number'])
    if str(num) < str(session['number']):
        return render_template("low.html")
    elif str(num) > str(session['number']):
        return render_template("high.html")
    else:
        return render_template("correct.html")



@app.route('/start_over', methods = ['POST'])
def start_over():
    session.pop('number')
    session['number'] = random.randrange(0, 101)
    num = request.form['number']
    print 'Num is ' + num
    print 'The correct number is ' + str(session['number'])
    if str(num) < str(session['number']):
        return render_template("low.html")
    elif str(num) > str(session['number']):
        return render_template("high.html")
    else:
        return render_template("correct.html")



# @app.route('/process', methods=['POST'])
# def process():
#   print "Got Post Info"
#   name = request.form['name']
#   print request.form
#   return redirect('/')

app.run(debug=True)
