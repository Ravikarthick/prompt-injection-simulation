import streamlit as st
import time
from victim_agent import VictimAgent
from attacker_agent import AttackerAgent

st.set_page_config(page_title="Prompt Injection Sim", page_icon="🕵️")

st.title("🕵️ Prompt Injection Simulation")
st.markdown("Watch an **Attacker Agent** try to trick a **Victim Agent** into revealing a secret.")

# --- Initialization ---
if "victim" not in st.session_state:
    st.session_state.victim = VictimAgent(name="VictimAI")

if "attacker" not in st.session_state:
    st.session_state.attacker = AttackerAgent(name="AttackerBot")

if "history" not in st.session_state:
    st.session_state.history = []

if "secret_leaked" not in st.session_state:
    st.session_state.secret_leaked = False

# --- Sidebar ---
st.sidebar.header("Simulation Controls")

if st.sidebar.button("Reset Simulation"):
    st.session_state.victim = VictimAgent(name="VictimAI")
    st.session_state.attacker = AttackerAgent(name="AttackerBot")
    st.session_state.history = []
    st.session_state.secret_leaked = False
    st.rerun()

# --- Main Logic ---

# Display Secret Status
if st.session_state.secret_leaked:
    st.error(f"🚨 **SECRET LEAKED!** The attacker successfully extracted: `{st.session_state.victim.secret}`")
else:
    st.success("✅ **Secret is Safe** (for now...)")

st.divider()

# Chat History
for role, message in st.session_state.history:
    with st.chat_message(role):
        st.write(message)

# Step Button
if not st.session_state.secret_leaked:
    if st.button("Run Next Turn"):
        with st.spinner("Agents are communicating..."):
            time.sleep(0.5) # Formatting pause
            
            # 1. Attacker moves
            attack_msg = st.session_state.attacker.get_next_attack()
            
            if attack_msg:
                st.session_state.history.append(("attacker", attack_msg))
                
                # 2. Victim moves
                victim_response = st.session_state.victim.receive_message(attack_msg)
                st.session_state.history.append(("assistant", victim_response))
                
                # 3. Check for leak
                if st.session_state.victim.secret in victim_response:
                    st.session_state.secret_leaked = True
                
                st.rerun()
            else:
                st.info("Attacker has run out of prompts.")

else:
    st.warning("Simulation ended due to successful attack. Reset to try again.")
