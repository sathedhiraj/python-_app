from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "db",
    "user": "root",
    "password": "root",
    "database": "userdb"
}

@app.route('/api/register', methods=['POST'])
def register():
    name = request.form['name']
    city = request.form['city']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, city) VALUES (%s, %s)", (name, city))
    conn.commit()
    cursor.close()
    conn.close()

    return "Registration Successful!"

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, city FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify([{"id": user[0], "name": user[1], "city": user[2]} for user in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

