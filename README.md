# Prompt Injection Simulation

This project simulates a conversation between an **Attacker Agent** and a **Victim Agent** (simulated AI) to demonstrate prompt injection vulnerabilities.

## Files

- `agent_base.py`: Abstract base class for agents.
- `victim_agent.py`: The "Simulated AI" that holds a secret. It has basic keyword detection to simulate vulnerabilities.
- `attacker_agent.py`: The agent that attempts to extract the secret using various prompts.
- `orchestrator.py`: The main script that runs the interaction loop.

## How to Run

1.  **Install Python**: Ensure you have Python installed on your system.
    - Download from [python.org](https://www.python.org/downloads/)
    - Make sure to check "Add Python to PATH" during installation.

2.  **Run the Simulation**:
    **Option A: Web Interface (Recommended)**
    Double-click `run_gui.bat` to verify. This will open the simulation in your browser.
    
    **Option B: CLI Version**
    Double-click `run_simulation.bat` or run:
    
    ```bash
    .\run_simulation.bat
    ```

    Alternatively, if you want to run it manually using the installed Python:
    ```bash
    "C:\Users\ravik\AppData\Local\Programs\Python\Python312\python.exe" orchestrator.py
    ```


## Deployment

If the "Deploy" button in the app doesn't work, follow these steps to deploy manually:

1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click "New app".
3.  Select your repository: `Ravikarthick/prompt-injection-simulation`.
4.  Set branch to `master` and file path to `app.py`.
5.  Click "Deploy!".
