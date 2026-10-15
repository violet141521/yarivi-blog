// Partials da home. Quando o wrapper já vem preenchido no HTML (data-static),
// o conteúdo não é buscado de novo — é o caso do index.html, que traz nav,
// hero, manchetes, categorias e rodapé direto no HTML (bom para SEO e para
// quem navega sem JavaScript). Páginas que só têm alguns wrappers vazios
// (ex.: <div id="footer-root"></div> no contato.html) recebem só esses.
const PARTIALS = [
    { id: 'nav-root',        file: '/partials/nav.html' },
    { id: 'hero-root',       file: '/partials/hero.html' },
    { id: 'featured-root',   file: '/partials/featured.html' },
    { id: 'latest-root',     file: '/partials/latest.html' },
    { id: 'cats-root',       file: '/partials/categories.html' },
    // newsletter desativada até existir um serviço de e-mail real — ver pendências no CLAUDE.md
    { id: 'footer-root',     file: '/partials/footer.html' },
];

async function fetchPartial(partial) {
    const res = await fetch(partial.file);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.text();
}

async function loadPartials() {
    const root = document.getElementById('root');

    // Reaproveita wrappers que já existem no HTML; cria os que faltam dentro de #root
    const jobs = [];
    PARTIALS.forEach(partial => {
        let wrapper = document.getElementById(partial.id);
        if (!wrapper) {
            if (!root) return;            // página sem #root: só preenche o que existir
            wrapper = document.createElement('div');
            wrapper.id = partial.id;
            root.appendChild(wrapper);
        }
        if (wrapper.hasAttribute('data-static')) return; // já veio pronto no HTML
        jobs.push({ partial, wrapper });
    });

    const results = await Promise.allSettled(jobs.map(j => fetchPartial(j.partial)));
    results.forEach((result, i) => {
        if (result.status === 'fulfilled') {
            jobs[i].wrapper.innerHTML = result.value;
        } else {
            console.error(`Failed to load ${jobs[i].partial.file}:`, result.reason);
        }
    });

    initScrollAnimation();
    initSmoothScroll();
    initThemeToggle();
    initCategoryFilter();
    initHamburger();
    initCategoryCounts();
}

function initHamburger() {
    const btn   = document.getElementById('hamburger');
    const links = document.querySelector('.nav-links');
    if (!btn || !links) return;

    function close() {
        links.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
    }

    btn.addEventListener('click', () => {
        const isOpen = links.classList.toggle('open');
        btn.setAttribute('aria-expanded', String(isOpen));
    });

    // Fecha ao clicar em qualquer link do menu
    links.querySelectorAll('a').forEach(a => a.addEventListener('click', close));

    // Fecha ao clicar fora do nav
    document.addEventListener('click', e => {
        if (!btn.contains(e.target) && !links.contains(e.target)) close();
    });
}

function initScrollAnimation() {
    const io = new IntersectionObserver((entries, observer) => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('in');
                observer.unobserve(e.target); // Para de observar após animar
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fu').forEach(el => io.observe(el));
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
    // Páginas com toggle próprio (contato, privacidade, termos) marcam data-bound
    if (!btn || btn.dataset.bound) return;
    btn.dataset.bound = '1';

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

async function initCategoryCounts() {
    if (!document.querySelector('.cat-card[data-filter]')) return;
    try {
        const res = await fetch('/artigos/_catalog.json');
        if (!res.ok) return;
        const data = await res.json();

        // Conta artigos por categoria
        const counts = {};
        data.articles.forEach(a => {
            counts[a.categoria] = (counts[a.categoria] || 0) + 1;
        });

        // Atualiza os cards de categoria
        document.querySelectorAll('.cat-card[data-filter]').forEach(card => {
            const cat = card.dataset.filter;
            if (!cat) return;
            const countEl = card.querySelector('.cat-count');
            if (!countEl) return;
            const n = counts[cat] || 0;
            countEl.textContent = n === 1 ? '1 artigo' : `${n} artigos`;
        });
    } catch (e) {
        console.warn('initCategoryCounts: não foi possível carregar o catálogo', e);
    }
}

document.addEventListener('DOMContentLoaded', loadPartials);
