from flask import Flask,redirect,url_for,jsonify,request
app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"


@app.route("/getdata")
def getData():
    return jsonify({"Name":request.args["name"],"EmpCode": request.args["empcode"]})

#throws error but works after comment
#if __name__ == "__main__" 
#app.run(debug=True,port=8000)
app.run() ##Can also be used as a default option





