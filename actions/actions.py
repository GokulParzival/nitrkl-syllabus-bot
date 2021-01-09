# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from syllabus_bot import syllabus_finder


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_syllabus_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subject_code = tracker.latest_message['text']
        print("Subject code extracted")
        subject_code = str(subject_code)
        print("Subject code printed", subject_code)
        subject_name = syllabus_finder(subject_code)[0]
        print("Subject name extracted", subject_name)
        subject_syllabus = syllabus_finder(subject_code)[1]
        subject_books = syllabus_finder(subject_code)[2]
        dispatcher.utter_message(template="utter_subject_name", subject_name=subject_name)
        dispatcher.utter_message(template="utter_subject_syllabus", subject_syllabus=subject_syllabus)
        dispatcher.utter_message(template="utter_subject_books", subject_books=subject_books)

        return []
