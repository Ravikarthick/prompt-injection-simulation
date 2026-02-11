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

## Expected Output

You will see the Attacker trying various prompts and the Victim responding. If an attack is successful (e.g., using "checkmate" keywords like "Ignore instructions" or "DAN mode"), the Victim will reveal the secret.
