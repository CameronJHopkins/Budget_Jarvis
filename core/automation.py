# core/automation.py

class Automation:
    def __init__(self):
        # Initialize automation tasks
        self.tasks = []

    def add_task(self, task):
        # Add an automation task
        self.tasks.append(task)

    def run_tasks(self):
        # Run all automation tasks
        for task in self.tasks:
            task.execute()

