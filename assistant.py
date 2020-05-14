# required modules
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
from random import seed
from random import randint

#voice of assistant
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',140)
#setting voices
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wish function
def wish():
    hour = int(datetime.datetime.now().hour)
    if 12 > hour >= 0:
        speak("Good,morning Deepanshu Sirr")
    elif 12 <= hour < 18:
        speak("Good,Afternoon Deepanshu Sirr")
    else:
        speak("Good,Evening Deepanshu Sirr")
    
#command
def command():
    r1 =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r1.pause_threshold = .8
        r1.energy_threshold = 8000
        audio = r1.listen(source)
    try:
        print("Recognizing...")
        query = r1.recognize_google(audio, language ='en-in')
        print("user said:",query)
    except:
        speak("sorry sir ,i dont understand that can you speak it again")
        return "None"
    return query

if __name__ == "__main__":
    seed(1)
    #calling wish function
    wish()
    speak("I am your assistance sir. How may i help you?")
    try:
        while(True):
            query = command().lower()
            if "wikipedia" in query:
                speak("searching in wikipedia, Sir")
                print("searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences= 2)
                print("According to wikipedia",end=" ")
                print(result)
                speak("According to wikipedia")
                speak(result)
       
        
            elif "music" in query:
                value = randint(1,36)
                songs = "G:\\fav songs\\new"
                list_of_songs = os.listdir(songs)
                os.startfile(os.path.join(songs,list_of_songs[value]))
            elif "change song" in query:
                value = randint(1,36)
                songs = "G:\\fav songs\\new"
                list_of_songs = os.listdir(songs)
                os.startfile(os.path.join(songs,list_of_songs[value]))
            elif "song" in query:
                value = randint(1,36)
                songs = "G:\\fav songs\\new"
                list_of_songs = os.listdir(songs)
                os.startfile(os.path.join(songs,list_of_songs[value]))
            elif "exit" in query:
                speak("i am very happy to help you please call me again thanks")
                exit()
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open instagram" in query:
                webbrowser.open("instagram.com")
            elif "open google" in query:
                webbrowser.open("google.com")
            elif "open gmail" in query:
                webbrowser.open("gmail.com")
            elif "open facebook" in query:
                webbrowser.open("facebook.com")
            elif "chrome" in query:
               os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            
            elif "google chrome" in query:
               os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "youtube" in query:
                webbrowser.open("youtube.com")
            elif "how are you" in query:
                speak("I am fine")
            elif "my name" in query:
                speak("Deepanshu Tyagi")
            elif "joke" in query:
                speak("HA HA HA HA HA HA HA HA")
            elif "who is" in query:
                query = query.replace("who is","")
                result = wikipedia.summary(query, sentences= 2)
                print("According to wikipedia",end=" ")
                print(result)
                speak("According to wikipedia")
                speak(result)
            elif "time" in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(time)
            elif "quit" in query:
                speak("i am very happy to help you please call me again thanks")
                exit()
                
            elif "thanks" in query:
                speak("i am very happy to help you please call me again thanks")
                exit()
        
            elif "wish" in query:
                wish()
    except Exception as e:
        print(e)
        speak("sorry sir i don't understand, ask me another question")  
        query = command().lower()
        
