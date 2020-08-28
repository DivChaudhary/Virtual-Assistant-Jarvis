import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import psutil
import pyjokes
import requests
import json

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!") 
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis,how may I help you")       

def takeCommand():
    """
    Takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"    
    
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def takeSnap():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\DIV CHAUDHARY\\Desktop\\Python\\a.png")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery()
    print(battery)

def climate():
    speak("Please Enter the city name")
    city = input("City Name: ")
    url =  "http://api.openweathermap.org/data/2.5/weather?q={}&appid=fd42803ff8f720819345518a2c8ec0e8".format(city)
    res = requests.get(url)
    data = res.json()
    desc = data['weather'][0]['description']
    print("Description: ",desc)

if __name__ == "__main__":
    wishMe()
    while(1):
        query = takeCommand().lower()    
    
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")    
        elif 'open geeks for geeks' in query:
            webbrowser.open("www.geeksforgeeks.org")
        elif 'play music' in query:
            music_dir = 'H:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\DIV CHAUDHARY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to ajay' in query:
            try:
                speak("What is the message")
                content = takeCommand()
                to = "ajaymgc@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry sir,I am unable to send this email currently.")
        elif 'remember that' in query:
            speak('What should I remember?')
            data = takeCommand()
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif 'remind me' in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" + remember.read())
            remember.close()
        elif 'take screenshot' in query:
            takeSnap()
            speak("Screenshot Taken")
        elif 'cpu' in query:
            cpu()
        elif 'weather' in query:
            climate()
        elif 'shutdown' in query:
            os.system('shutdown /p /f')            
        elif 'go offline' in query:
            exit()                