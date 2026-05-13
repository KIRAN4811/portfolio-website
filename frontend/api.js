// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Fetch all projects
async function fetchProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`);
        if (!response.ok) {
            throw new Error('Failed to fetch projects');
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching projects:', error);
        return [];
    }
}

// Fetch single project
async function fetchProject(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/projects/${id}`);
        if (!response.ok) {
            throw new Error('Failed to fetch project');
        }
        return await response.json();
    } catch (error) {
        console.error('Error fetching project:', error);
        return null;
    }
}

// Add new project
async function addProject(projectData) {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(projectData),
        });
        if (!response.ok) {
            throw new Error('Failed to add project');
        }
        return await response.json();
    } catch (error) {
        console.error('Error adding project:', error);
        return null;
    }
}

// Update project
async function updateProject(id, projectData) {
    try {
        const response = await fetch(`${API_BASE_URL}/projects/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(projectData),
        });
        if (!response.ok) {
            throw new Error('Failed to update project');
        }
        return await response.json();
    } catch (error) {
        console.error('Error updating project:', error);
        return null;
    }
}

// Delete project
async function deleteProject(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/projects/${id}`, {
            method: 'DELETE',
        });
        if (!response.ok) {
            throw new Error('Failed to delete project');
        }
        return await response.json();
    } catch (error) {
        console.error('Error deleting project:', error);
        return null;
    }
}

// Submit contact form
async function submitContactForm(contactData) {
    try {
        const response = await fetch(`${API_BASE_URL}/contacts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(contactData),
        });
        if (!response.ok) {
            throw new Error('Failed to submit contact form');
        }
        return await response.json();
    } catch (error) {
        console.error('Error submitting contact form:', error);
        return null;
    }
}
