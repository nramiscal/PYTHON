from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def greeting():
    return render_template("index.html")

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")

@app.route("/dojos")
def dojos():
    return render_template("dojos.html")

@app.route("/dojos/new", methods=['POST'])
def subscribe():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    print request.form
    return redirect("/dojos")

app.run(debug = True)