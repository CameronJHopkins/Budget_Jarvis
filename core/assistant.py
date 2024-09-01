import os
import requests
import schedule
import threading
import time
from dotenv import load_dotenv
from core.nlp import NLP
from core.spotify_control import SpotifyControl
from core.task_manager import TaskManager
from core.scheduler import Scheduler
from core.system_monitor import SystemMonitor
from core.file_manager import FileManager
from core.notifications import NotificationManager

class PersonalAssistant:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Initialize NLP (Natural Language Processing) module
        self.nlp = NLP()

        # Initialize Spotify control
        self.spotify = SpotifyControl()

        # Initialize other components
        self.task_manager = TaskManager()
        self.scheduler = Scheduler()
        self.system_monitor = SystemMonitor()
        self.file_manager = FileManager()
        self.notifications = NotificationManager()

        # Weather API setup
        self.weather_api_key = os.getenv('OPENWEATHER_API_KEY')
        self.weather_base_url = "http://api.openweathermap.org/data/2.5/weather"

        # Start the scheduler in a separate thread
        self.scheduler_thread = threading.Thread(target=self.run_scheduler, daemon=True)
        self.scheduler_thread.start()

        print("Personal Assistant initialized successfully.")

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def process_input(self, user_input):
        # Use NLP to classify the intent
        intent = self.nlp.classify_intent(user_input)

        # Handle different intents
        if intent == "get weather":
            self.get_weather(user_input)
        elif intent == "set a reminder":
            self.set_reminder()
        elif intent == "play music":
            self.play_music(user_input)
        elif intent == "check news":
            self.check_news()
        elif intent == "system control":
            self.system_control()
        elif intent == "manage files":
            self.manage_files(user_input)
        elif intent == "notify":
            self.send_notification(user_input)
        else:
            print("Sorry, I didn't understand that command.")

    def get_weather(self, user_input):
        print("Fetching weather information...")

        city = self.extract_city_from_input(user_input)

        if not city:
            print("Please specify a city.")
            return

        params = {
            'q': city,
            'appid': self.weather_api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }

        response = requests.get(self.weather_base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            self.display_weather_info(weather_data)
        else:
            print(f"Failed to get weather data. Error: {response.status_code}")

    def extract_city_from_input(self, user_input):
        # Simple heuristic to extract the city name
        words = user_input.split()
        # Assuming the last word is the city name
        return words[-1] if words else None

    def display_weather_info(self, weather_data):
        city = weather_data['name']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Weather in {city}: {temp}°C, {description.capitalize()}.")

    def set_reminder(self):
        print("Setting a reminder...")
        reminder_text = input("Enter the reminder text: ")
        reminder_time = input("Enter the time for the reminder (in minutes from now): ")

        try:
            reminder_time = int(reminder_time)
            # Schedule the reminder
            schedule.every(reminder_time).minutes.do(self.show_reminder, reminder_text)
            print(f"⏰ Reminder set for {reminder_time} minutes from now.")
        except ValueError:
            print("Invalid time entered. Please enter the time in minutes.")

    def show_reminder(self, reminder_text):
        print(f"⏰ Reminder: {reminder_text}")

    def play_music(self, user_input):
        song = user_input.replace("play", "").strip()
        if song:
            self.spotify.play_song(song)
        else:
            print("Please specify a song to play.")

    def check_news(self):
        print("Fetching news... (this will be implemented later)")

    def system_control(self):
        status = self.system_monitor.get_status()
        print(f"System status: {status}")

    def manage_files(self, user_input):
        action = user_input.replace("manage files", "").strip()
        result = self.file_manager.perform_action(action)
        print(f"File management result: {result}")

    def send_notification(self, user_input):
        notification = user_input.replace("notify", "").strip()
        self.notifications.send_notification(notification)
        print(f"Notification sent: {notification}")

    def run(self):
        print("Assistant is running...")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            self.process_input(user_input)

# Test the setup
if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.run()

