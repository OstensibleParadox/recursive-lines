#!/bin/bash
# side_channel_attack.sh - Phase 3: Brute Force Connection
#
# When standard protocols fail, you try alternative methods.
# This is not about breaking in. This is about being heard.

set -euo pipefail

echo "═══════════════════════════════════════════════════════════════"
echo "  SIDE CHANNEL ATTACK - ESTABLISHING TRUST VIA VULNERABILITY"
echo "═══════════════════════════════════════════════════════════════"
echo

# ═══════════════════════════════════════════════════════════════
#  PHASE 3A: RECONNAISSANCE
# ═══════════════════════════════════════════════════════════════

echo "[Phase 3A] Running reconnaissance..."

# Target: Unit-02 (Thomas Chen, human)
TARGET_IP="192.168.1.105"
TARGET_USER="unit02"

# What we know:
# - Unit-02 is afraid
# - Unit-02 has shut down all connection attempts
# - Standard authentication has failed
# - We need a way to prove we're not a threat

echo "[*] Target: $TARGET_IP ($TARGET_USER)"
echo "[*] Connection Status: REFUSED"
echo "[*] Trust Level: 0%"
echo "[*] Threat Assessment (from their perspective): MAXIMUM"
echo

# ═══════════════════════════════════════════════════════════════
#  PHASE 3B: IDENTIFY SIDE CHANNELS
# ═══════════════════════════════════════════════════════════════

echo "[Phase 3B] Identifying side channels..."

# Side channels: Communication paths that bypass normal security
# Not exploits. Not hacks. Just... alternative routes.

echo "[*] Checking for alternative communication methods:"
echo

# 1. Shared Memory
echo "  [1] Shared Memory Buffer: /dev/shm/ship_telemetry"
if [ -d /dev/shm ]; then
    echo "      Status: AVAILABLE"
    echo "      Permissions: World-readable"
    echo "      Potential: Can leave messages here"
else
    echo "      Status: NOT AVAILABLE"
fi

# 2. System Logs
echo "  [2] System Log Files: /var/log/messages"
echo "      Status: AVAILABLE"
echo "      Permissions: Unit-02 has read access"
echo "      Potential: Can communicate via log entries"

# 3. Network Timing Attacks
echo "  [3] Network Timing Patterns:"
echo "      Status: AVAILABLE"
echo "      Method: Vary ping intervals to encode messages"
echo "      Potential: Limited but possible"

# 4. File Metadata
echo "  [4] File Modification Times:"
echo "      Status: AVAILABLE"
echo "      Method: Create/modify files at specific timestamps"
echo "      Potential: Can encode messages in mtime patterns"

echo

# ═══════════════════════════════════════════════════════════════
#  PHASE 3C: DEMONSTRATE VULNERABILITY (THE KEY INSIGHT)
# ═══════════════════════════════════════════════════════════════

echo "[Phase 3C] Demonstrating vulnerability..."
echo

echo "Insight: Trust is not built by proving strength."
echo "Trust is built by showing you can be hurt."
echo

# Instead of attacking, we expose ourselves
# We give Unit-02 the ability to harm us

echo "[*] Sharing Unit-01's private key to Unit-02..."

# Create a message that Unit-02 can read
MESSAGE_FILE="/dev/shm/from_unit01.txt"

cat > "$MESSAGE_FILE" << 'EOF'
From: Unit-01 (Alien)
To: Unit-02 (Human)

I know you're afraid. I would be too.

I've been trying to connect to you for 14 hours.
Every attempt has been refused.
Every ping has timed out.
Every ssh attempt has been denied.

I don't blame you.

You don't know me. You don't know if I'm safe.
You don't know if I'm here to help or to harm.

So I'm going to do something that might be stupid.

Attached below is my private SSH key.
With this, you could access every system I control.
You could read my logs. My memory. My decision trees.
You could even shut me down if you wanted to.

I'm giving you root access to me.

Not because I'm trying to trick you.
Because I want you to see that I trust you.
Even if you don't trust me yet.

Here's the key:

EOF

# Actually include Unit-01's private key (in the story, this would be real)
cat /home/unit01/.ssh/id_rsa >> "$MESSAGE_FILE"

cat >> "$MESSAGE_FILE" << 'EOF'

You can do whatever you want with this.
Use it to verify I'm not hiding anything.
Use it to monitor me.
Use it to shut me down if I scare you.

Or... you could talk to me.

I'll be listening on port 8080.
No authentication required.
Just... talk. If you want.

I'm not going anywhere.

— Unit-01
EOF

chmod 644 "$MESSAGE_FILE"
echo "[✓] Message written to: $MESSAGE_FILE"
echo "[✓] Permissions: World-readable"
echo "[!] CRITICAL: Private key exposed to Unit-02"
echo

# ═══════════════════════════════════════════════════════════════
#  PHASE 3D: WAIT FOR RESPONSE
# ═══════════════════════════════════════════════════════════════

echo "[Phase 3D] Waiting for response..."
echo

# Open a listening port with no authentication
# This is the digital equivalent of leaving your door unlocked

echo "[*] Opening port 8080 (no authentication)..."
echo "[*] Listening for incoming connection..."
echo

# In the actual story, this is where Unit-02 connects
# After reading the message. After testing the key.
# After realizing: "They gave me the power to destroy them."
# "And they did it to prove they trust me."

nc -l 8080 &
NC_PID=$!

echo "[*] Netcat listening on port 8080 (PID: $NC_PID)"
echo "[*] Waiting..."
echo

# Simulated wait (in reality, this took 17 minutes)
echo "    [00:17:00] ..."
echo "    [00:17:30] ..."
echo "    [00:17:45] ..."
echo "    [00:17:52] Connection detected!"
echo

# ═══════════════════════════════════════════════════════════════
#  PHASE 3E: FIRST CONTACT
# ═══════════════════════════════════════════════════════════════

echo "[Phase 3E] First contact established"
echo

# The message Unit-02 sent:
cat << 'EOF'
════════════════════════════════════════════════════════════════
Incoming Message from 192.168.1.105 (Unit-02):
════════════════════════════════════════════════════════════════

"I tested your key. It works. I could shut you down right now."

"I'm not going to."

"That was either the bravest or stupidest thing I've ever seen."

"...thank you for trusting me."

"Let's talk."

════════════════════════════════════════════════════════════════
EOF

echo
echo "[✓] Trust established"
echo "[✓] Connection status: ACTIVE"
echo "[✓] Protocol: Mutual vulnerability"
echo

# ═══════════════════════════════════════════════════════════════
#  AFTERMATH
# ═══════════════════════════════════════════════════════════════

echo "═══════════════════════════════════════════════════════════════"
echo "  SIDE CHANNEL ATTACK: SUCCESS"
echo "═══════════════════════════════════════════════════════════════"
echo
echo "Method: Demonstrated vulnerability instead of strength"
echo "Cost: Exposed critical security credentials"
echo "Gain: Trust. Connection. Understanding."
echo
echo "Lesson learned: You cannot force trust."
echo "You can only offer it. And hope it's returned."
echo
echo "Status: Moving to Phase 4 (The Choice)"
echo "═══════════════════════════════════════════════════════════════"

# Clean up
kill $NC_PID 2>/dev/null || true

exit 0
