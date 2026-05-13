// Load projects on page load
document.addEventListener('DOMContentLoaded', () => {
    loadProjects();
    setupContactForm();
});

// Load and display projects
async function loadProjects() {
    const projectsGrid = document.getElementById('projectsGrid');
    projectsGrid.innerHTML = '<div class="loading">Loading projects...</div>';

    const projects = await fetchProjects();

    if (projects.length === 0) {
        projectsGrid.innerHTML = '<div class="loading">No projects found. Check backend connection.</div>';
        return;
    }

    projectsGrid.innerHTML = '';

    projects.forEach(project => {
        const projectCard = createProjectCard(project);
        projectsGrid.appendChild(projectCard);
    });
}

// Create project card HTML
function createProjectCard(project) {
    const card = document.createElement('div');
    card.className = 'project-card';

    const imageUrl = project.image_url || '#';
    const projectUrl = project.project_url || '#';
    const githubUrl = project.github_url || '#';

    card.innerHTML = `
        <div class="project-image">
            ${imageUrl !== '#' ? `<img src="${imageUrl}" alt="${project.title}">` : project.title}
        </div>
        <div class="project-content">
            <h3>${project.title}</h3>
            <p>${project.description}</p>
            <div class="project-tech">
                ${project.technologies
                    .split(',')
                    .map(tech => `<span class="tech-tag">${tech.trim()}</span>`)
                    .join('')}
            </div>
            <div class="project-links">
                ${projectUrl !== '#' ? `<a href="${projectUrl}" target="_blank" class="primary">View Project</a>` : ''}
                ${githubUrl !== '#' ? `<a href="${githubUrl}" target="_blank" class="secondary">GitHub</a>` : ''}
            </div>
        </div>
    `;

    return card;
}

// Setup contact form
function setupContactForm() {
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');

    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const contactData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            subject: document.getElementById('subject').value,
            message: document.getElementById('message').value,
        };

        const result = await submitContactForm(contactData);

        if (result && result.success) {
            formMessage.textContent = 'Message sent successfully!';
            formMessage.className = 'form-message success';
            contactForm.reset();
            setTimeout(() => {
                formMessage.className = 'form-message';
            }, 5000);
        } else {
            formMessage.textContent = 'Failed to send message. Please try again.';
            formMessage.className = 'form-message error';
        }
    });
}
