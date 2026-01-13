from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)

    return render_template("index.html")

app.run(debug=True)