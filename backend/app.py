import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'portfolio_db')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/projects', methods=['GET'])
def get_projects():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM projects ORDER BY created_at DESC')
        projects = cur.fetchall()
        cur.close()
        return jsonify(projects), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/projects', methods=['POST'])
def add_project():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO projects (title, description, technologies, github_url) VALUES (%s, %s, %s, %s)',
            (data['title'], data['description'], data['technologies'], data.get('github_url', ''))
        )
        mysql.connection.commit()
        cur.close()
        return jsonify({'success': True}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contacts', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)',
            (data['name'], data['email'], data['subject'], data['message'])
        )
        mysql.connection.commit()
        cur.close()
        return jsonify({'success': True}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
