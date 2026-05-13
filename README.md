# Portfolio Website

A full-stack portfolio website built with HTML/CSS/JavaScript frontend, Flask backend, and MySQL database.

## Features

- Responsive Design - Works on all devices
- Project Showcase - Display your projects dynamically
- Contact Form - Collect visitor messages
- Admin API - Manage projects via REST API
- MySQL Database - Persistent data storage

## Quick Start

### 1. Database Setup

mysql -u root -p < backend/database/schema.sql

### 2. Backend Setup

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py

Backend runs on: http://localhost:5000

### 3. Frontend Setup

cd frontend
python -m http.server 8000

Frontend runs on: http://localhost:8000
