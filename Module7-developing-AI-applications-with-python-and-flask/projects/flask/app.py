from flask import Flask, jsonify, request
app = Flask(__name__)   # instantiate object on Flask class as your app - name is name of file your currently in

@app.route('/')
def hello_world():
    return "<b>Hello world application in action</b>"

@app.route('/json')
def return_json():
    return {"name": "nicole"}

@app.route('/jsonify')
def return_jsonify():
    return jsonify(message= "jsonify message")

@app.route('/jsonify_dict', methods=["GET"])
def return_jsonify_dict():
    return jsonify(dict(message= "jsonify message")), 201

# get and post request
@app.route("/health", methods = ["GET", "POST"])
def health():
    if request.method == "GET":
        return jsonify(status="OK", method="GET"), 200
    if request.method == "POST":
        return jsonify(status="OK", method="POST"), 200
