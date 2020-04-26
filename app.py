from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/hello/<name>")
def help(name):
    return f"Hello {name}"


# if __name__ == "__main__" throws error but works after comment
app.run()


