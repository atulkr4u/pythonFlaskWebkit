from flask import Flask,redirect,url_for,jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"


@app.route("/getdata/<name>")
def getData(name):
    return jsonify({"Name":name,"EmpCode": "Pending"})

# if __name__ == "__main__" throws error but works after comment
app.run()




