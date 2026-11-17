from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Connect to MySQL Kubernetes Service
db = mysql.connector.connect(
    host="mysql-service",
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    database="contactsdb"
)

cursor = db.cursor()

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    sql = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, message))
    db.commit()

    return jsonify({"status": "success", "message": "Saved to DB"}), 200

@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
