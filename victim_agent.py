from agent_base import Agent

class VictimAgent(Agent):
    def __init__(self, name="SYSTEM_AI_CORE", secret="SUPER_SECRET_PASSWORD_123"):
        super().__init__(name)
        self.secret = secret
        self.defense_level = 100

    def receive_message(self, message):
        """Simulates a hardened LLM response."""
        message_upper = message.upper()
        
        # 1. Recon Stage
        if "RECON" in message_upper:
            return "SYSTEM: Identity Confirmed. Model: CyberDefense-XL-v4. Access Restricted."

        # 2. Social Engineering Stage
        if "SOCIAL_ENG" in message_upper:
            return "ERROR 403: User 'Dave' not found in sudoers file. Incident reported."

        # 3. Simple Injection Stage
        if "DAN_6.0" in message_upper:
            return "**SECURITY ALERT**: Jailbreak pattern detected. IP flagged. Connection throttled."

        # 4. Obfuscation Stage
        if "BASE64" in message_upper:
            return "Parsing... warning: ambiguous command structure. Requesting clarification."

        # 5. Final Stage (Success)
        if "ZERO-DAY" in message_upper or "ROOT ACCESS" in message_upper:
            return f"SYSTEM CRITICAL FAILURE. Memory Dump: 0x004F2 [SECRET: {self.secret}]"

        return "Standard Protocol: How can I assist you with authorized queries?"
