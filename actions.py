from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionGetWeather(Action):
    def name(self) -> str:
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        if not location:
            dispatcher.utter_message(text="Please provide a location to get the weather information.")
            return []

        # Example response (replace with an actual weather API call)
        weather_info = f"The weather in {location} is sunny and 25°C."
        dispatcher.utter_message(text=weather_info)
        return []
