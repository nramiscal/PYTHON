from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def ninja():
  return render_template("ninja.html")

@app.route('/ninja/<color>')
def show_ninja(color):
    if color == "blue":
        return render_template("color.html", name = "leonardo")
    elif color == "orange":
        return render_template("color.html", name = "michelangelo")
    elif color == "red":
        return render_template("color.html", name = "raphael")
    elif color == "purple":
        return render_template("color.html", name = "donatello")
    else:
        return render_template("color.html", name = "notapril")


# @app.route('/ninja/blue')
# def blue():
#   return render_template("blue.html")

# @app.route('/ninja/orange')
# def orange():
#   return render_template("orange.html")

# @app.route('/ninja/red')
# def red():
#   return render_template("red.html")

# @app.route('/ninja/purple')
# def purple():
#   return render_template("purple.html")



app.run(debug=True)