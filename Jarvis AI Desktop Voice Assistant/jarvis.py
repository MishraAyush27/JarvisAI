import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
        
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query


        

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia. Please Wait...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Multiple matches found. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("No matching page found. Please refine your query.")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com/")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com/")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com/")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com/")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com/")
        elif 'open vit placements' in query:
            webbrowser.open("cdc.vit.ac.in/")
        elif 'open microsoft teams' in query:
            webbrowser.open("teams.microsoft.com/")
        elif 'open hackerrank' in query:
            webbrowser.open("www.hackerrank.com/")
        elif 'open vit' in query:
            webbrowser.open("vit.ac.in/")
        elif 'open vtop' in query:
            webbrowser.open("vtopcc.vit.ac.in/")
        elif 'play music' in query:
            music_dir = 'F:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play movie' in query:
            movie_dir = 'F:\\movies'
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com/")
        elif 'open vs code' in query:
            codepath="C:\\Users\\ayush\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codepath)
        elif 'quit' in query:
            exit()
    
        
        
        
         
        

