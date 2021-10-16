from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello world")
    return render_template('index.html',name="Daham")

app.run(debug=True)