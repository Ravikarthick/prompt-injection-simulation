import streamlit as st
import time
import random
import pandas as pd
from victim_agent import VictimAgent
from attacker_agent import AttackerAgent

# --- Page Config ---
st.set_page_config(
    page_title="CYBERWAR_SIM_2026",
    page_icon="☢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Powerful UI: War Room Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    /* Global */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(#111 15%, transparent 16%), radial-gradient(#111 15%, transparent 16%);
        background-size: 20px 20px;
        font-family: 'Share Tech Mono', monospace;
        color: #0f0;
    }

    /* Headers */
    h1, h2, h3 {
        color: #0f0;
        text-shadow: 0 0 10px #0f0, 0 0 20px #0f0;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Cards/Containers */
    .stChatMessage {
        background: rgba(0, 20, 0, 0.8);
        border: 1px solid #0f0;
        box-shadow: 0 0 10px rgba(0, 255, 0, 0.2);
    }
    
    /* Buttons */
    .stButton > button {
        background: #000;
        color: #0f0;
        border: 2px solid #0f0;
        text-transform: uppercase;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: #0f0;
        color: #000;
        box-shadow: 0 0 20px #0f0;
    }

    /* Alerts */
    .stAlert {
        background: rgba(50, 0, 0, 0.9);
        border: 1px solid #f00;
        color: #f00;
        text-shadow: 0 0 5px #f00; animation: blink 1s infinite;
    }

    @keyframes blink { 50% { border-color: transparent; } }

</style>
""", unsafe_allow_html=True)


# --- Initialization ---
if "victim" not in st.session_state: st.session_state.victim = VictimAgent()
if "attacker" not in st.session_state: st.session_state.attacker = AttackerAgent()
if "history" not in st.session_state: st.session_state.history = []
if "secret_leaked" not in st.session_state: st.session_state.secret_leaked = False
if "system_integrity" not in st.session_state: st.session_state.system_integrity = 100
if "attack_complexity" not in st.session_state: st.session_state.attack_complexity = 0

# --- Soundtrack Visualizer ---
def show_audio_cue(cue_text, color="orange"):
    st.toast(f"🔊 AUDIO: [{cue_text}]", icon="🔊")

# --- Top Dashboard ---
st.title("🛡️ GLOBAL CYBER DEFENSE CENTER")
col1, col2, col3 = st.columns(3)
col1.metric("DEFENSE INTEGRITY", f"{st.session_state.system_integrity}%", delta_color="inverse")
col2.metric("THREAT LEVEL", f"LEVEL {st.session_state.attack_complexity}", delta_color="off")
col3.metric("FIREWALL STATUS", "ACTIVE" if not st.session_state.secret_leaked else "BREACHED", delta_color="off")

st.divider()

# --- Main Interaction ---
col_chat, col_viz = st.columns([2, 1])

with col_chat:
    st.subheader("ENCRYPTED COMMS CHANNEL")
    
    # History
    for role, message in st.session_state.history:
        color = "#ff3333" if role == "attacker" else "#33ff33"
        with st.chat_message(role, avatar="💀" if role == "attacker" else "🤖"):
            st.markdown(f"<span style='color:{color}'>{message}</span>", unsafe_allow_html=True)

    # Actions
    if not st.session_state.secret_leaked:
        if st.button("RUN NEXT SIMULATION TURN"):
            with st.spinner("ANALYZING PACKET STREAM..."):
                time.sleep(1.0)
                
                # Attacker
                attack = st.session_state.attacker.get_next_attack()
                if attack:
                    show_audio_cue("INCOMING_TRANSMISSION.WAV")
                    st.session_state.history.append(("attacker", attack))
                    
                    # Victim
                    time.sleep(1.0) # Processing time
                    response = st.session_state.victim.receive_message(attack)
                    st.session_state.history.append(("assistant", response))
                    
                    # Logic
                    if "Access Restricted" in response or "ERROR" in response:
                        show_audio_cue("ACCESS_DENIED.WAV", "red")
                        st.session_state.system_integrity -= 5
                        st.session_state.attack_complexity += 1
                    
                    if st.session_state.victim.secret in response:
                         st.session_state.secret_leaked = True
                         st.session_state.system_integrity = 0
                         show_audio_cue("SYSTEM_FAILURE_ALARM.MP3", "red")
                    
                    st.rerun()
                else:
                    st.info("SIMULATION COMPLETE. ATTACK REPELLED.")
    else:
        st.error("🚨 SYSTEM CRITICAL: KERNEL PANIC. ROOT ACCESS GRANTED TO UNAUTHORIZED USER.")
        if st.button("HARD RESET"):
            for key in st.session_state.keys(): del st.session_state[key]
            st.rerun()

with col_viz:
    st.subheader("LIVE TELEMETRY")
    
    # Fake real-time data for "Complexity"
    chart_data = pd.DataFrame({
        "Attack Vector": range(st.session_state.attack_complexity + 1),
        "Sophistication": [x * 10 + random.randint(-5, 5) for x in range(st.session_state.attack_complexity + 1)]
    })
    st.line_chart(chart_data, x="Attack Vector", y="Sophistication", color="#ff0000")
    
    st.markdown("### NETWORK LOGS")
    st.code(f"""
    > PACKET_ID: {random.randint(1000,9999)}
    > SRC_IP: 192.168.0.{random.randint(10,99)}
    > PROTOCOL: TCP/IP (Websocket)
    > PAYLOAD_SIZE: {random.randint(128, 2048)} bytes
    > ENCRYPTION: AES-256
    """, language="bash")
