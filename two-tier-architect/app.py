from flask import Flask, jsonify
from flask_cors import CORS  # You may need to run: pip install flask-cors

app = Flask(__name__)
CORS(app)  # This allows the frontend to talk to this backend

@app.route("/api/data")
def get_data():
    # This simulates data coming from a database
    return jsonify({
        "message": "Hello from the Flask Backend!",
        "status": "Online",
        "engineer": "DevOps Hero"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)