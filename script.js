const PARTIALS = [
    { id: 'nav-root',        file: 'partials/nav.html' },
    { id: 'hero-root',       file: 'partials/hero.html' },
    { id: 'featured-root',   file: 'partials/featured.html' },
    { id: 'latest-root',     file: 'partials/latest.html' },
    { id: 'cats-root',       file: 'partials/categories.html' },
    // { id: 'nl-root',      file: 'partials/newsletter.html' }, // desativado temporariamente — ver pendências no CLAUDE.md
    { id: 'footer-root',     file: 'partials/footer.html' },
];

async function loadPartials() {
    const root = document.getElementById('root');

    for (const partial of PARTIALS) {
        const wrapper = document.createElement('div');
        wrapper.id = partial.id;
        root.appendChild(wrapper);
        try {
            const res = await fetch(partial.file);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            wrapper.innerHTML = await res.text();
        } catch (e) {
            console.error(`Failed to load ${partial.file}:`, e);
        }
    }

    initScrollAnimation();
    initNewsletter();
    initSmoothScroll();
    initThemeToggle();
    initCategoryFilter();
}

function initScrollAnimation() {
    const io = new IntersectionObserver(entries => {
        entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('.fu').forEach(el => io.observe(el));
}

function initNewsletter() {
    const form = document.getElementById('nl-form');
    if (!form) return;
    form.addEventListener('submit', e => {
        e.preventDefault();
        const btn = document.getElementById('nl-btn');
        const input = e.target.querySelector('input');
        btn.textContent = '✓ Inscrito!';
        btn.style.background = '#3DFFD0';
        input.value = '';
        setTimeout(() => {
            btn.textContent = 'Quero receber';
            btn.style.background = '';
        }, 3000);
    });
}

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            const target = document.querySelector(a.getAttribute('href'));
            if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
        });
    });
}

function initThemeToggle() {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        btn.textContent = theme === 'light' ? '☀️' : '🌙';
        localStorage.setItem('yarivi-theme', theme);
    }

    applyTheme(localStorage.getItem('yarivi-theme') || 'dark');

    btn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        applyTheme(current === 'light' ? 'dark' : 'light');
    });
}

function initCategoryFilter() {
    document.addEventListener('click', e => {
        const catCard = e.target.closest('[data-filter]');
        if (!catCard) return;

        const filter = catCard.dataset.filter;
        const isActive = catCard.classList.contains('active');

        document.querySelectorAll('[data-filter]').forEach(c => c.classList.remove('active'));
        document.querySelectorAll('[data-category]').forEach(card => card.classList.remove('hidden'));

        if (!isActive && filter) {
            // Filtro de categoria — ativar nav-link e cat-card correspondentes
            document.querySelectorAll(`[data-filter="${filter}"]`).forEach(c => c.classList.add('active'));
            document.querySelectorAll('[data-category]').forEach(card => {
                if (card.dataset.category !== filter) card.classList.add('hidden');
            });
        } else {
            // Início ou clique no mesmo filtro — mostrar tudo e ativar Início
            document.querySelectorAll('[data-filter=""]').forEach(c => c.classList.add('active'));
        }
    });
}

document.addEventListener('DOMContentLoaded', loadPartials);
