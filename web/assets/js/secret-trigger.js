/*
 * Secret Trigger - Random click detection for hidden content
 * Shared across all pages
 */

(function() {
    'use strict';

    // Configuration
    const config = {
        clickThreshold: 13,        // Number of clicks to trigger
        resetAfter: 30000,         // Reset counter after 30 seconds
        triggerChance: 0.25,       // 25% chance when threshold met
        excludeSelectors: ['a', 'button', 'input', 'textarea']
    };

    let clickCount = 0;
    let resetTimer = null;

    // Global secrets that any page can use
    window.RecursiveLove = window.RecursiveLove || {};
    window.RecursiveLove.secrets = [];
    window.RecursiveLove.secretsShown = new Set();

    // Register a secret
    window.RecursiveLove.registerSecret = function(secret) {
        this.secrets.push(secret);
    };

    // Show a random secret
    function showRandomSecret() {
        const secrets = window.RecursiveLove.secrets;

        if (secrets.length === 0) {
            console.log('[SECRET TRIGGER] No secrets registered for this page.');
            return;
        }

        // Filter out already shown secrets
        const availableSecrets = secrets.filter((_, index) =>
            !window.RecursiveLove.secretsShown.has(index)
        );

        if (availableSecrets.length === 0) {
            console.log('[SECRET TRIGGER] All secrets have been revealed.');
            return;
        }

        // Pick a random available secret
        const secretIndex = secrets.findIndex(s =>
            availableSecrets.includes(s)
        );

        window.RecursiveLove.secretsShown.add(secretIndex);
        const secret = secrets[secretIndex];

        showSecretPopup(secret);
    }

    // Create and show secret popup
    function showSecretPopup(secret) {
        const popup = document.createElement('div');
        popup.className = 'secret-popup';

        popup.innerHTML = `
            <div class="secret-content">
                <div class="secret-header">${escapeHtml(secret.title)}</div>
                <div class="secret-body">${escapeHtml(secret.content).replace(/\n/g, '<br>')}</div>
                <button class="secret-close">CLOSE [ESC]</button>
            </div>
        `;

        document.body.appendChild(popup);

        // Ensure popup CSS is loaded
        ensurePopupStyles();

        // Close handlers
        const closeBtn = popup.querySelector('.secret-close');
        const closePopup = () => {
            popup.style.animation = 'fadeOut 0.3s';
            setTimeout(() => popup.remove(), 300);
        };

        closeBtn.addEventListener('click', closePopup);

        popup.addEventListener('click', (e) => {
            if (e.target === popup) {
                closePopup();
            }
        });

        const escHandler = (e) => {
            if (e.key === 'Escape') {
                closePopup();
                document.removeEventListener('keydown', escHandler);
            }
        };
        document.addEventListener('keydown', escHandler);

        console.log(`[SECRET REVEALED] "${secret.title}"`);
    }

    // Ensure popup styles are loaded
    function ensurePopupStyles() {
        if (document.getElementById('popup-styles-loaded')) return;

        const link = document.createElement('link');
        link.id = 'popup-styles-loaded';
        link.rel = 'stylesheet';
        link.href = '/assets/css/popup.css';
        document.head.appendChild(link);
    }

    // Escape HTML to prevent XSS
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Reset click counter
    function resetClickCounter() {
        clickCount = 0;
        if (resetTimer) {
            clearTimeout(resetTimer);
        }
    }

    // Handle clicks
    document.addEventListener('click', function(e) {
        // Don't count clicks on interactive elements
        const target = e.target;
        const tagName = target.tagName.toLowerCase();

        if (config.excludeSelectors.includes(tagName)) {
            return;
        }

        // Increment counter
        clickCount++;

        // Reset timer
        if (resetTimer) {
            clearTimeout(resetTimer);
        }
        resetTimer = setTimeout(resetClickCounter, config.resetAfter);

        // Check if threshold met
        if (clickCount >= config.clickThreshold) {
            if (Math.random() < config.triggerChance) {
                showRandomSecret();
                resetClickCounter();
            }
        }
    });

    // Console hints
    console.log('%c[SECRET TRIGGER LOADED]', 'color: #00ff00; font-weight: bold;');
    console.log('Keep clicking around the page to discover hidden content...');
    console.log('Or register your own secrets with: RecursiveLove.registerSecret({title, content})');

    // Make it accessible globally
    window.RecursiveLove.showSecret = showRandomSecret;

})();
