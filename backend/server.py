from flask import Flask, jsonify
from flask_cors import CORS

# App instance
app = Flask(__name__)

# Cross-origin resource sharing
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
  return jsonify({
    "message": "Hello world!"
  })

if __name__ == "__main__":
  app.run(debug=True, port=5328)