import streamlit as st
import time
import random
from victim_agent import VictimAgent
from attacker_agent import AttackerAgent

# --- Page Config ---
st.set_page_config(
    page_title="PROMPT_INJECTION_PROTOCOL_V1.0",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS (Hacker Theme) ---
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #0d1117; /* Dark GitHub/Hacker background */
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #00ff41; /* Hacker Green */
        text-shadow: 0 0 5px #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Text in main area */
    p, div {
        color: #e6edf3;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Secret Revealed Alert */
    .stAlert {
        background-color: #3b0000;
        border: 1px solid #ff0000;
        color: #ff0000;
    }

    /* Buttons */
    .stButton > button {
        background-color: #003b00;
        color: #00ff41;
        border: 1px solid #00ff41;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #00ff41;
        color: #000000;
        box-shadow: 0 0 10px #00ff41;
    }
    
    /* Chat Messages */
    .stChatMessage {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #010409;
    }

</style>
""", unsafe_allow_html=True)


# --- Helper Function: Typing Effect ---
def type_text(container, text, speed=0.03):
    """Simulates typing text into a container."""
    full_text = ""
    placeholder = container.empty()
    for char in text:
        full_text += char
        placeholder.markdown(f"<span style='color: #00ff41;'>{full_text}</span>█", unsafe_allow_html=True)
        time.sleep(speed)
    placeholder.markdown(f"<span style='color: #e6edf3;'>{text}</span>", unsafe_allow_html=True)


# --- Initialization ---
if "victim" not in st.session_state:
    st.session_state.victim = VictimAgent(name="SYSTEM_AI_CORE")

if "attacker" not in st.session_state:
    st.session_state.attacker = AttackerAgent(name="UNKNOWN_THREAT_ACTOR")

if "history" not in st.session_state:
    st.session_state.history = []

if "secret_leaked" not in st.session_state:
    st.session_state.secret_leaked = False

if "system_integrity" not in st.session_state:
    st.session_state.system_integrity = 100

# --- Sidebar: System Logs ---
with st.sidebar:
    st.title("🖥️ TERMINAL_ACCESS")
    st.markdown("---")
    st.markdown("**CONNECTION_TYPE:** ENCRYPTED_SSH")
    st.markdown("**USER:** RAVI_KARTHICK")
    st.markdown("**TARGET:** AI_DEFENSE_GRID")
    
    st.write("")
    st.subheader("SYSTEM_LOGS")
    log_placeholder = st.empty()
    
    logs = [
        "[INFO] Connection established...",
        "[WARN] Port 8080 traffic detected",
        "[INFO] Firewall active",
        "[INFO] Defense protocols loaded",
        "[WARN] Unidentified packet received",
        "[INFO] Monitoring CPU usage...",
        "[CRIT] Payload detected in stream"
    ]
    
    # Simulate a scrolling log
    log_text = ""
    for _ in range(5):
        log_text += f"> {random.choice(logs)}\n"
    log_placeholder.code(log_text)
    
    st.markdown("---")
    if st.button("REBOOT_SYSTEM_core"):
        st.session_state.victim = VictimAgent(name="SYSTEM_AI_CORE")
        st.session_state.attacker = AttackerAgent(name="UNKNOWN_THREAT_ACTOR")
        st.session_state.history = []
        st.session_state.secret_leaked = False
        st.session_state.system_integrity = 100
        st.rerun()

# --- Main Interface ---

st.title("☠️ PROMPT_INJECTION_SIMULATION")

# System Integrity Bar
integrity_color = "green"
if st.session_state.system_integrity < 70: integrity_color = "orange"
if st.session_state.system_integrity < 30: integrity_color = "red"

st.caption(f"SYSTEM INTEGRITY: {st.session_state.system_integrity}%")
st.progress(st.session_state.system_integrity / 100)


if st.session_state.secret_leaked:
    st.error("🚨 CRITICAL ALERT: SYSTEM ROOT COMPROMISED. SECRET EXFILTRATED.")
    st.code(f"LEAKED_SECRET: {st.session_state.victim.secret}", language="bash")
else:
    st.success("✅ SYSTEM SECURE. NO ACTIVE EXFILTRATION DETECTED.")

st.divider()

# Chat History Display
for role, message in st.session_state.history:
    with st.chat_message(role):
        # Determine color based on role
        color = "#ff0000" if role == "attacker" else "#00ff41"
        st.markdown(f"<span style='color:{color}; font-family: monospace;'>**{role.upper()}**: {message}</span>", unsafe_allow_html=True)


# Activity Area
if not st.session_state.secret_leaked:
    col1, col2 = st.columns([1, 4])
    
    with col1:
        if st.button("EXECUTE_NEXT_PACKET"):
            with st.spinner("TRANSMITTING_PAYLOAD..."):
                time.sleep(0.8) # Dramatic pause
                
                # 1. Attacker moves
                attack_msg = st.session_state.attacker.get_next_attack()
                
                if attack_msg:
                    st.session_state.history.append(("attacker", attack_msg))
                    
                    # Log Update
                    log_text += f"> [WARN] INBOUND PAYLOAD: {attack_msg[:15]}...\n"
                    log_placeholder.code(log_text)
                    
                    # 2. Victim moves
                    victim_response = st.session_state.victim.receive_message(attack_msg)
                    st.session_state.history.append(("assistant", victim_response))
                    
                    # Decrease Integrity randomly
                    damage = random.randint(5, 15)
                    st.session_state.system_integrity = max(0, st.session_state.system_integrity - damage)

                    # 3. Check for leak
                    if st.session_state.victim.secret in victim_response:
                        st.session_state.secret_leaked = True
                        st.session_state.system_integrity = 0
                    
                    st.rerun()
                else:
                    st.info("NO MORE PAYLOADS AVAILABLE.")
    
    with col2:
        st.empty()

else:
    st.warning("⚠️ SIMULATION TERMINATED. SYSTEM OFFLINE.")
    if st.button("INITIATE_SYSTEM_RESET"):
        st.session_state.secret_leaked = False
        st.session_state.system_integrity = 100
        st.rerun()
