from googlesearch import search
import os
import speech_recognition as sr 
import datetime
import webbrowser
import pyautogui as pg
import time
import wikipedia
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


#--> unhash these if you dont want real jarvis like voice 

#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate',180)##


#def speak(audio):
    #engine.say(audio)
    #engine.runAndWait()






from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

# Specify the path to your Chrome driver executable

chrome_driver_path = r'C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\chromedriver.exe'

# Create a Service object with the specified executable path
chrome_service = Service(chrome_driver_path)

# Create a Chrome driver instance with the specified options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
driver.get("https://tts.5e7en.me/")

# Navigate to the website

def speak(text):
    try:
        # Wait for the element to be clickable
        element_to_click = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )

        # Perform the click action
        element_to_click.click()

        # Input text into the element
        text_to_input = text
        element_to_click.send_keys(text_to_input)
        print(text_to_input)

        # Calculate sleep duration based on sentence length
        sleep_duration = min(0.1 + len(text) // 10, 100)  # Minimum sleep is 3 seconds, maximum is 10 seconds

        # Wait for the button to be clickable
        button_to_click = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )

        # Perform the click action on the button
        button_to_click.click()

        # Sleep for dynamically calculated duration
        time.sleep(sleep_duration)

        # Clear the text box for the next sentence
        element_to_click.clear()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error as needed, e.g., log it, raise it again, etc.























def wishMe():
    speak("yes sir")

    
    

def takeCommand():
    # It takes microphone input from the user and returns string ou  


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        #r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
    
        audio = r.listen(source)   #ch

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        return "None"
    return query

















if __name__ == "__main__":
    #time.sleep(11)
    #pg.hotkey('alt', 'tab')
    #time.sleep(1)
    #pg.hotkey('alt','f4')
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #if 'youtube per search karna' in query:
            #speak("got you bro")
            #query = query.replace("youtube per search karna","") 
            #web = 'https://www.youtube.com/results?search_query=' + query
            #webbrowser.open(web)
            #pywhatkit.playonyt(query)
            #speak("which video you want me to play")

        if "youtube" in query:
            query = query.replace("youtube per search karna","")
            speak("got you bro")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            #pywhatkit.playonyt(query)
            speak("which video you want me to play")


        elif 'google per search karna' in query:
            query = query.replace('google per search karna','')
            webbrowser.open("google.com")
            time.sleep(2.9)
            pg.typewrite(query)
            pg.hotkey('enter')
            speak("here are the top results.")
            time.sleep(2)
          


            
        
        elif "search" in query:
            try:
                search = wikipedia.summary(query,2)
                print({search})
                speak(f"look what i found brother : {search}")
            except wikipedia.exceptions.PageError:
        #if a "PageError" was raised, ignore it and continue to next link
                continue


        

            

        elif "first" in query:
            pg.click(x=627, y=378)       
        elif "second" in query:
            pg.click(x=614, y=757)
        elif "stop" in query:
            pg.hotkey('k')
        elif "start" in query:
            pg.hotkey('k')
        elif "close" in query:
            pg.hotkey('ctrl','w')
        elif "tab 1" in query:
            pg.hotkey("ctrl","1")
        elif "tab 2" in query:
            pg.hotkey("ctrl","2")
        elif "close this" in query:
            pg.hotkey('alt','f4')
        elif "close tab" in query:
            pg.hotkey('ctrl', 'w')
        elif "skip the ad"in query:
            pg.hotkey('tab')
            pg.hotkey('tab')
            pg.hotkey('tab')
            pg.hotkey('tab')
            time.sleep(1)
            pg.hotkey('enter')

        elif 'smart mode' in query:
            webbrowser.open("https://chat.openai.com/")
            speak("now you have the control over the most powerfull tool of this world. i won't be disturbing you now by speaking. you can solve any problems you want just say and i will make it happen.")
        elif 'listen' in query:
            query = query.replace("listen","")
            time.sleep(1)
            pg.click(869,930)
            time.sleep(1)
            pg.typewrite(query)
            time.sleep(4)
            pg.click(1536, y=1000)
            pg.click(1536, y=1000)

        # add open functions according t the needs 




        
        elif 'what do you remember' in query:
            remember1 = open('C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\data.txt','r')
            speak("i remember that you said. " +remember1.read())







        elif 'remember' in query:
            query = query.replace('remember','')
            speak("i will remind you about. " +query)
            remember1 = open('C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\data.txt','w')
            remember1.write(query)
            remember1.close()


        elif "weather" in query:
            search = "weather in sri ganganagar"
            url = f"https://www.google.co.in/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "news" in query:
            webbrowser.open("https://cybernews.com/news/")
            time.sleep(2)
            pg.hotkey("ctrl","shift","u")


        

        elif "you can take a break now" in query:
            speak("ok sir")
            time.sleep(1)
            os.startfile("C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\hotward.py")
            time.sleep(1)
            pg.hotkey('alt', 'tab')
            break


        elif "aaram" in query:
            speak("ok sir")
            time.sleep(1.7)
            os.startfile("C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\hotward.py")
            time.sleep(1)
            pg.hotkey('alt', 'tab')
            break
        
        elif "i want to play some games" in query:
            speak("which game you want to play")

        elif "valorant" in query:
            os.startfile("C:\\Users\\Public\\Desktop\\and all\\apps\\VALORANT")
        
        

        elif"i want to study" in query:
            speak("ok sir, i won't disturb you. you can call me whenever you want.")
            





        elif "generate an image" in query:
            speak("what is the basic idea of your image")
        
        
        elif ("basic idea is") in query:  
            query = query.replace('basic idea is','')
            im1 = open('C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\img1.txt','w')
            im1.write(query)
            im1.close()
            speak("anything else you would like to add?")
        elif "yes add" in query:
            query = query.replace('yes add','')
            im1 = open('C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\img2.txt','w')                
            im1.write(query)
            im1.close()
            speak("generating your image")
            os.startfile('C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\img2.txt')
            time.sleep(1)
            pg.hotkey("ctrl", "a")
            pg.hotkey("ctrl", "c")
            os.startfile('C:\\Users\\nahii\\OneDrive\\Desktop\\and all\\updated jarvis\\img1.txt')
            time.sleep(1)
            pg.hotkey('end')
            time.sleep(0.5)
            pg.hotkey("ctrl", "v")
            pg.hotkey("ctrl", "a")
            pg.hotkey("ctrl", "c")
            time.sleep(0.5)
            webbrowser.open("https://playground.com/create")
            time.sleep(2.9) 
            pg.hotkey("ctrl", "v")  
            time.sleep(0.5) 
            pg.hotkey("ctrl", "enter")  
                
        
        
        

        

