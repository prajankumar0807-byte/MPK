# Flask example for admin user management
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

@app.route('/admin/users', methods=['GET'])
def get_all_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mpk_db"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/admin/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Verify admin role here
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mpk_db"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User deleted successfully"})