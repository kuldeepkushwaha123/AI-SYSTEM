import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evining!")

    speak("i am jarvis sir. please tell me how may i help you")

def takecommand():
    # """ ye command is function me jarvis ke sun ne ke kaam ayega """

    r = sr.Recognizer()
    with sr.Microphone() as sorce:
        r.pause_threshould = 1
        audio = r.listen(sorce)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        return "none"
    return query



if __name__=="__main__" :
     wishMe()
     while True:
         query = takecommand().lower()

     # yaha pe ham logic lagayenge command ke liye
         if "wikipedia" in query:
           speak('searching wikipedia...')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           print(results)
           speak(results)
         elif 'open youtube' is query:
            webbrowser.open("youtube.com")

         elif 'open google' is query:
             webbrowser.open("google.com")

         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir, the time is {strTime}")





