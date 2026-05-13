import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'portfolio_db')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Routes

# Health check
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

# Get all projects
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

# Get single project
@app.route('/api/projects/<int:id>', methods=['GET'])
def get_project(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM projects WHERE id = %s', (id,))
        project = cur.fetchone()
        cur.close()
        if project:
            return jsonify(project), 200
        return jsonify({'error': 'Project not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add new project
@app.route('/api/projects', methods=['POST'])
def add_project():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['title', 'description', 'technologies']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO projects (title, description, technologies, image_url, project_url, github_url) VALUES (%s, %s, %s, %s, %s, %s)',
            (
                data['title'],
                data['description'],
                data['technologies'],
                data.get('image_url', ''),
                data.get('project_url', ''),
                data.get('github_url', '')
            )
        )
        mysql.connection.commit()
        project_id = cur.lastrowid
        cur.close()

        return jsonify({'success': True, 'id': project_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update project
@app.route('/api/projects/<int:id>', methods=['PUT'])
def update_project(id):
    try:
        data = request.get_json()

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM projects WHERE id = %s', (id,))
        project = cur.fetchone()

        if not project:
            cur.close()
            return jsonify({'error': 'Project not found'}), 404

        # Update fields
        cur.execute(
            'UPDATE projects SET title = %s, description = %s, technologies = %s, image_url = %s, project_url = %s, github_url = %s WHERE id = %s',
            (
                data.get('title', project['title']),
                data.get('description', project['description']),
                data.get('technologies', project['technologies']),
                data.get('image_url', project['image_url']),
                data.get('project_url', project['project_url']),
                data.get('github_url', project['github_url']),
                id
            )
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'success': True, 'message': 'Project updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete project
@app.route('/api/projects/<int:id>', methods=['DELETE'])
def delete_project(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM projects WHERE id = %s', (id,))
        project = cur.fetchone()

        if not project:
            cur.close()
            return jsonify({'error': 'Project not found'}), 404

        cur.execute('DELETE FROM projects WHERE id = %s', (id,))
        mysql.connection.commit()
        cur.close()

        return jsonify({'success': True, 'message': 'Project deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Submit contact form
@app.route('/api/contacts', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Basic email validation
        if '@' not in data['email']:
            return jsonify({'error': 'Invalid email address'}), 400

        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)',
            (
                data['name'],
                data['email'],
                data['subject'],
                data['message']
            )
        )
        mysql.connection.commit()
        contact_id = cur.lastrowid
        cur.close()

        return jsonify({'success': True, 'id': contact_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all contacts (for admin)
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = cur.fetchall()
        cur.close()
        return jsonify(contacts), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
