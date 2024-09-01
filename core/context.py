# core/context.py

import json

class ContextManager:
    def __init__(self):
        self.context_file = 'data/context_data.json'
        self.context_data = self.load_context()

    def load_context(self):
        # Load context data from file
        if os.path.exists(self.context_file):
            with open(self.context_file, 'r') as f:
                return json.load(f)
        return {}

    def save_context(self):
        # Save context data to file
        with open(self.context_file, 'w') as f:
            json.dump(self.context_data, f, indent=4)

    def update_context(self, key, value):
        # Update context data and save to file
        self.context_data[key] = value
        self.save_context()

    def get_context(self, key):
        # Retrieve context data
        return self.context_data.get(key, None)

