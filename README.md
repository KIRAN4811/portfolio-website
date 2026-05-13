# Portfolio Website

A full-stack portfolio website built with HTML/CSS/JavaScript frontend, Flask backend, and MySQL database.

## 🎨 Features

- **Responsive Design** - Works on all devices
- **Project Showcase** - Display your projects dynamically
- **Contact Form** - Collect visitor messages
- **Admin API** - Manage projects via REST API
- **MySQL Database** - Persistent data storage

## 📁 Project Structure

```
portfolio-website/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── responsive.css
│   ├── script.js
│   └── api.js
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env.example
│   └── database/
│       └── schema.sql
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- Node.js (optional, for local server)

### 1. Database Setup

```bash
# Login to MySQL
mysql -u root -p

# Create database and tables
source backend/database/schema.sql;
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your MySQL credentials

# Run Flask app
python app.py
```

Backend will run on `http://localhost:5000`

### 3. Frontend Setup

```bash
cd frontend

# Using Python's built-in server
python -m http.server 8000

# Or using Node.js http-server
npx http-server -p 8000
```

Frontend will run on `http://localhost:8000`

## 📚 API Endpoints

### Get All Projects
```
GET /api/projects
```

### Get Single Project
```
GET /api/projects/<id>
```

### Add Project
```
POST /api/projects
Content-Type: application/json

{
  "title": "Project Title",
  "description": "Project description",
  "technologies": "Python, Flask, MySQL",
  "image_url": "url-to-image",
  "project_url": "https://project-link.com",
  "github_url": "https://github.com/link"
}
```

### Update Project
```
PUT /api/projects/<id>
Content-Type: application/json

{
  "title": "Updated Title",
  "description": "Updated description",
  "technologies": "Updated tech stack",
  "image_url": "new-image-url",
  "project_url": "updated-project-url",
  "github_url": "updated-github-url"
}
```

### Delete Project
```
DELETE /api/projects/<id>
```

### Submit Contact Form
```
POST /api/contacts
Content-Type: application/json

{
  "name": "Your Name",
  "email": "your.email@example.com",
  "subject": "Message Subject",
  "message": "Your message"
}
```

## 🌐 Deployment

### Deploy Frontend to Netlify

1. Push your repo to GitHub
2. Connect your repo to Netlify
3. Set build settings:
   - Build command: (leave empty)
   - Publish directory: `frontend`
4. Deploy!

### Deploy Backend to Heroku/Railway

#### Option 1: Heroku

```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set DB_HOST=your-db-host
heroku config:set DB_USER=your-db-user
heroku config:set DB_PASSWORD=your-db-password
heroku config:set DB_NAME=portfolio_db

# Deploy
git push heroku main
```

#### Option 2: Railway

1. Connect GitHub repo to Railway
2. Add MySQL plugin
3. Set environment variables
4. Deploy

## 🔧 Environment Variables

Create a `.env` file in the backend directory:

```
FLASK_ENV=development
FLASK_DEBUG=True
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=portfolio_db
```

## ✏️ Customization

### Update Portfolio Information

1. Edit `frontend/index.html` - Update name, bio, and social links
2. Add your projects via the API or directly in the database
3. Customize colors in `frontend/styles.css`

### Add Your Bank Management System Project

Use the API:

```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Bank Management System",
    "description": "A DBMS project implementing a comprehensive bank management system with account management, transactions, and customer database.",
    "technologies": "DBMS, SQL, Database Design",
    "image_url": "path-to-image",
    "project_url": "#",
    "github_url": "https://github.com/KIRAN4811/bank-management-system"
  }'
```

## 🐛 Troubleshooting

### MySQL Connection Error
- Check MySQL is running
- Verify credentials in `.env`
- Ensure database is created

### CORS Errors
- Make sure Flask is running on `http://localhost:5000`
- Check CORS is enabled in `app.py`

### Port Already in Use
- Change port in `app.py` or `http-server` command
- Kill process using the port

### Frontend Not Loading
- Make sure you're in the `frontend` directory
- Check if `http://localhost:8000` is accessible
- Clear browser cache and refresh

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Kiran** - [GitHub Profile](https://github.com/KIRAN4811)
