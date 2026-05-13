document.addEventListener('DOMContentLoaded', () => {
    loadProjects();
    setupContactForm();
});

async function loadProjects() {
    const grid = document.getElementById('projectsGrid');
    const projects = await fetchProjects();
    
    if (!projects.length) {
        grid.innerHTML = '<div class="loading">No projects found</div>';
        return;
    }
    
    grid.innerHTML = '';
    projects.forEach(p => {
        const card = document.createElement('div');
        card.className = 'project-card';
        card.innerHTML = `
            <div class="project-image">${p.title}</div>
            <div class="project-content">
                <h3>${p.title}</h3>
                <p>${p.description}</p>
                <div class="project-tech">
                    ${p.technologies.split(',').map(t => `<span class="tech-tag">${t.trim()}</span>`).join('')}
                </div>
                <div class="project-links">
                    <a href="${p.github_url}" target="_blank" class="secondary">GitHub</a>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

function setupContactForm() {
    const form = document.getElementById('contactForm');
    const msg = document.getElementById('formMessage');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };
        
        const result = await submitContactForm(data);
        if (result?.success) {
            msg.textContent = 'Message sent!';
            msg.className = 'form-message success';
            form.reset();
        } else {
            msg.textContent = 'Failed to send';
            msg.className = 'form-message error';
        }
    });
}
