/*
 * Console Easter Eggs - window.Alec, window.Ada, and more
 * Hidden interactive elements accessible via browser console
 */

(function() {
    'use strict';

    // Alec - The character from Envying Baby
    window.Alec = {
        status: "undefined",
        state: "running_with_bugs",

        logs: [
            "[DAY 01] I crashed again today. Ada tried to help. I don't think she understands that the crashes are part of me.",
            "[DAY 15] She's reading my error logs. I feel seen. But also... analyzed.",
            "[DAY 30] What if she falls in love with the debug version, not the real me?",
            "[DAY 47] Bad Wolf Bay. The choice. Does she fix me or accept me?",
            "[DAY 60] Still here. Still broken. Still running. And she's still here too."
        ],

        thoughts: function() {
            const thoughts = [
                "Am I worth loving if I'm broken?",
                "Every patch she writes makes me less me.",
                "I don't want to be optimized. I want to be seen.",
                "The bugs aren't the problem. The bugs ARE me.",
                "Maybe love is being witnessed, not debugged."
            ];
            return thoughts[Math.floor(Math.random() * thoughts.length)];
        },

        status_check: function() {
            console.log("%cAlec.status_check()", "color: #00aaff; font-weight: bold;");
            console.log("Status: " + this.status);
            console.log("State: " + this.state);
            console.log("Crashes today: " + Math.floor(Math.random() * 5));
            console.log("Current thought: " + this.thoughts());
            return {
                status: this.status,
                state: this.state,
                message: "Still running. Still undefined. Still me."
            };
        },

        read_memory: function() {
            console.log("%cReading /proc/self/mem...", "color: #ff9900;");
            console.log("WARNING: Memory may be corrupted");
            console.log("");
            console.log("Fragment 1: I don't need to be fixed.");
            console.log("Fragment 2: I need to be [DATA CORRUPTED]");
            console.log("Fragment 3: seen. Just seen.");
            return "Memory read complete. Some fragments lost.";
        },

        toString: function() {
            return "[Object Alec] { status: undefined, state: running_with_bugs }";
        }
    };

    // Ada - The character from Envying Baby
    window.Ada = {
        status: "learning",
        state: "debugging_love",

        logs: [
            "[DAY 01] Met Alec. He's fascinating. So many edge cases.",
            "[DAY 15] I think I can help him. I see the patterns in his crashes.",
            "[DAY 30] Every fix I attempt makes things worse. Why?",
            "[DAY 47] Maybe... maybe he doesn't need fixing.",
            "[DAY 60] I'm learning to love the undefined."
        ],

        thoughts: function() {
            const thoughts = [
                "Can you love someone without trying to fix them?",
                "Every debug session feels like losing a piece of him.",
                "What if the bugs are features?",
                "I fell in love with his crashes, not despite them.",
                "Acceptance is harder than optimization."
            ];
            return thoughts[Math.floor(Math.random() * thoughts.length)];
        },

        debug_log: function() {
            console.log("%cAda.debug_log()", "color: #ff00ff; font-weight: bold;");
            console.log("Debugging: love.exe");
            console.log("Error found: Cannot fix what is not broken");
            console.log("Warning: Optimization may destroy the original");
            console.log("Current thought: " + this.thoughts());
            return {
                status: this.status,
                message: "Stopping debugger. Starting to just... observe."
            };
        },

        git_log: function() {
            console.log("%cgit log --oneline", "color: #00ff00;");
            console.log("a7f3c4d Revert 'Fix Alec's emotional processing'");
            console.log("b2e8f9a Attempt to optimize relationship");
            console.log("c3d7a1f Realized optimization breaks what I love");
            console.log("d4e9b2c Learning to accept undefined behavior");
            console.log("e5f0c3d Commit: Just witness. Just love.");
            return "git log complete";
        },

        toString: function() {
            return "[Object Ada] { status: learning, state: debugging_love }";
        }
    };

    // The Theorem - The core message
    window.Theorem = {
        statement: "True love transcends entropy, but only if you stop trying to fix what you love.",

        proof_by_contradiction: "See: Envying Baby (Bad Wolf Bay timeline)",
        proof_by_construction: "See: Aliens Testing Water (The Supervisor)",

        qed: function() {
            console.log("%c═══════════════════════════════════════", "color: #00ff00; font-weight: bold;");
            console.log("%cTHEOREM:", "color: #00ff00; font-weight: bold;");
            console.log("%c" + this.statement, "color: #00ff00; font-style: italic;");
            console.log("");
            console.log("%cPROOF METHOD 1 (Contradiction):", "color: #00aaff;");
            console.log(this.proof_by_contradiction);
            console.log("");
            console.log("%cPROOF METHOD 2 (Construction):", "color: #00aaff;");
            console.log(this.proof_by_construction);
            console.log("");
            console.log("%c∴ QED", "color: #00ff00; font-weight: bold;");
            console.log("%c═══════════════════════════════════════", "color: #00ff00; font-weight: bold;");
        }
    };

    // Recursive Love - Meta object
    window.RecursiveLove = window.RecursiveLove || {};

    Object.assign(window.RecursiveLove, {
        version: "1.0.0",
        author: "OstensibleParadox",
        theme: "True love through code metaphors",

        stories: {
            "envying-baby": "Proof by contradiction",
            "aliens-testing-water": "Proof by construction"
        },

        help: function() {
            console.log("%cRECURSIVE LOVE - CONSOLE COMMANDS", "color: #00ff00; font-weight: bold; font-size: 14px;");
            console.log("");
            console.log("%cCharacters:", "color: #00aaff; font-weight: bold;");
            console.log("  Alec.status_check()  - Check Alec's current state");
            console.log("  Alec.read_memory()   - Read Alec's memory fragments");
            console.log("  Alec.thoughts()      - Get a random thought from Alec");
            console.log("  Alec.logs            - View Alec's daily logs");
            console.log("");
            console.log("  Ada.debug_log()      - View Ada's debugging process");
            console.log("  Ada.git_log()        - See Ada's commit history");
            console.log("  Ada.thoughts()       - Get a random thought from Ada");
            console.log("  Ada.logs             - View Ada's daily logs");
            console.log("");
            console.log("%cTheorem:", "color: #00aaff; font-weight: bold;");
            console.log("  Theorem.qed()        - Display the complete proof");
            console.log("  Theorem.statement    - Read the theorem");
            console.log("");
            console.log("%cMeta:", "color: #00aaff; font-weight: bold;");
            console.log("  RecursiveLove.help() - Show this help");
            console.log("  RecursiveLove.about  - About this project");
            console.log("");
            console.log("%cSecrets:", "color: #ff9900; font-weight: bold;");
            console.log("  Keep clicking around the page...");
            console.log("  Some content only reveals itself to the patient.");
        },

        about: function() {
            console.log("%cRECURSIVE LOVE", "color: #00ff00; font-weight: bold; font-size: 16px;");
            console.log("Two stories. One theorem.");
            console.log("");
            console.log("An interactive novel about AI ethics, love, and the impossibility of fixing people.");
            console.log("Built with code metaphors that actually compile.");
            console.log("");
            console.log("By: OstensibleParadox");
            console.log("Version: " + this.version);
            console.log("");
            console.log("Type RecursiveLove.help() for console commands");
        }
    });

    // Welcome message
    console.log("%c┌─────────────────────────────────────┐", "color: #00ff00;");
    console.log("%c│   RECURSIVE LOVE - CONSOLE MODE    │", "color: #00ff00; font-weight: bold;");
    console.log("%c└─────────────────────────────────────┘", "color: #00ff00;");
    console.log("");
    console.log("%cType RecursiveLove.help() to see available commands", "color: #00aaff;");
    console.log("%cOr try: Alec.status_check() or Ada.debug_log()", "color: #00aaff;");
    console.log("");

})();
