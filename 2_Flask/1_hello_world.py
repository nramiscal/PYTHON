from flask import Flask 
app = Flask(__name__) 
                         
@app.route('/')          
                         
                        
def hello_world():
  return "<h1>Hello World!</h1><p>My name is Nina</p>"

app.run(debug=True) 