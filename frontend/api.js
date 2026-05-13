const API_BASE_URL = 'http://localhost:5000/api';

async function fetchProjects() {
    try {
        const response = await fetch(`${API_BASE_URL}/projects`);
        if (!response.ok) throw new Error('Failed');
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        return [];
    }
}

async function submitContactForm(data) {
    try {
        const response = await fetch(`${API_BASE_URL}/contacts`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
