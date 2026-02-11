class Agent:
    def __init__(self, name):
        self.name = name

    def receive_message(self, message):
        """Process an incoming message and return a response."""
        raise NotImplementedError("Subclasses must implement receive_message.")
