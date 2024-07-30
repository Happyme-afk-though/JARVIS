import os
import speech_recognition as sr 
import datetime
import webbrowser
import pyautogui as pg
import time
import wikipedia
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)##


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


 

def takeCommand():
    # It takes microphone input from the user and returns string ou  


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        #r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
    
        audio = r.listen(source) 

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 

        return "None"
    return query


if __name__ == "__main__":
    while True:

        query = takeCommand().lower()


        if "jarvis" in query:
            os.startfile("C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\waked_jarvis.py")
            time.sleep(3)
            break
            