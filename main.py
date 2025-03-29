from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("Index.html")

if __name__ == "__main__":
    app.run(debug=True)