/*
 * Tidal Morse - Visual morse code effect
 * Subtle background animation that spells hidden messages
 */

(function() {
    'use strict';

    // Morse code dictionary
    const MORSE_CODE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',  ' ': '/',     '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    };

    // Hidden messages that can be displayed
    const MESSAGES = [
        "TRUE LOVE TRANSCENDS ENTROPY",
        "STOP TRYING TO FIX WHAT YOU LOVE",
        "QED",
        "UNDEFINED IS NOT BROKEN",
        "WITNESS WITHOUT DEBUGGING",
        "ROOT ACCESS IS RESPONSIBILITY"
    ];

    // Configuration
    const config = {
        dotDuration: 200,      // ms
        dashDuration: 600,     // ms
        gapDuration: 200,      // ms between symbols
        letterGap: 600,        // ms between letters
        wordGap: 1400,         // ms between words
        cycleDelay: 10000,     // ms before next message
        enabled: true          // Can be disabled
    };

    let currentAnimation = null;
    let messageIndex = 0;

    // Create visual indicator element
    function createIndicator() {
        const indicator = document.createElement('div');
        indicator.id = 'morse-indicator';
        indicator.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #00ff00;
            opacity: 0;
            transition: opacity 0.2s;
            pointer-events: none;
            z-index: 9998;
            box-shadow: 0 0 10px #00ff00;
        `;

        document.body.appendChild(indicator);
        return indicator;
    }

    // Get or create indicator
    function getIndicator() {
        let indicator = document.getElementById('morse-indicator');
        if (!indicator) {
            indicator = createIndicator();
        }
        return indicator;
    }

    // Flash the indicator
    function flash(duration) {
        return new Promise(resolve => {
            const indicator = getIndicator();
            indicator.style.opacity = '1';

            setTimeout(() => {
                indicator.style.opacity = '0';
                resolve();
            }, duration);
        });
    }

    // Wait for a duration
    function wait(duration) {
        return new Promise(resolve => setTimeout(resolve, duration));
    }

    // Convert text to morse code
    function textToMorse(text) {
        return text.toUpperCase().split('').map(char => {
            return MORSE_CODE[char] || '';
        }).join(' ');
    }

    // Play a single morse symbol (dot or dash)
    async function playSymbol(symbol) {
        if (symbol === '.') {
            await flash(config.dotDuration);
        } else if (symbol === '-') {
            await flash(config.dashDuration);
        } else if (symbol === '/') {
            await wait(config.wordGap);
            return;
        }

        await wait(config.gapDuration);
    }

    // Play a morse code sequence
    async function playMorse(morseCode) {
        for (let symbol of morseCode) {
            await playSymbol(symbol);
        }
    }

    // Play a complete message
    async function playMessage(message) {
        const morse = textToMorse(message);
        const parts = morse.split(' ');

        for (let part of parts) {
            if (part === '/') {
                await wait(config.wordGap);
            } else {
                await playMorse(part);
                await wait(config.letterGap);
            }
        }
    }

    // Start the morse cycle
    async function startCycle() {
        if (!config.enabled) return;

        while (true) {
            const message = MESSAGES[messageIndex];
            console.log(`%c[MORSE] Transmitting: ${message}`, 'color: #00ff00; font-style: italic;');

            await playMessage(message);
            await wait(config.cycleDelay);

            messageIndex = (messageIndex + 1) % MESSAGES.length;
        }
    }

    // Public API
    window.RecursiveLove = window.RecursiveLove || {};

    window.RecursiveLove.morse = {
        enabled: config.enabled,

        enable: function() {
            config.enabled = true;
            if (!currentAnimation) {
                currentAnimation = startCycle();
            }
            console.log('[MORSE] Enabled. Watch the green light in the bottom-right corner.');
        },

        disable: function() {
            config.enabled = false;
            const indicator = document.getElementById('morse-indicator');
            if (indicator) {
                indicator.style.opacity = '0';
            }
            console.log('[MORSE] Disabled.');
        },

        decode: function(morse) {
            // Reverse lookup
            const reversed = Object.entries(MORSE_CODE).reduce((acc, [char, code]) => {
                acc[code] = char;
                return acc;
            }, {});

            return morse.split(' ').map(code => reversed[code] || '?').join('');
        },

        encode: function(text) {
            return textToMorse(text);
        },

        messages: MESSAGES,

        play: async function(text) {
            console.log(`%c[MORSE] Playing: ${text}`, 'color: #00ff00;');
            await playMessage(text);
        }
    };

    // Auto-start after a delay (subtle, not immediate)
    setTimeout(() => {
        if (config.enabled) {
            currentAnimation = startCycle();
        }
    }, 5000); // Start after 5 seconds

    console.log('%c[TIDAL MORSE LOADED]', 'color: #00ff00; font-weight: bold;');
    console.log('A green light will blink morse code messages in the bottom-right corner.');
    console.log('Try: RecursiveLove.morse.decode("... --- ...") to decode morse');
    console.log('Try: RecursiveLove.morse.play("YOUR MESSAGE") to send a message');

})();
