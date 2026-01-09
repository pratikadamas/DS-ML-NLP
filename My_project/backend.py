from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json() #Flask receives the data:
    x = data["x"]
    y = data["y"]
    result = x + y
    return jsonify({"result": result}) #Flask processes it and sends back a result:

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
    
    
    
    # User (via Streamlit)  --->  Flask (does the calculation)
    #     ⬆                          ⬇
    #  Result shown in Streamlit  <---  Response from Flask

