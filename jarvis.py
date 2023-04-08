import pyttsx3
import speech_recognition as sp
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else :
        speak("Good Evening")

speak("Sir, I am your doremon, how may i help you")

def takeCommand():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said {query}")

    except Exception as e:
        print("Say again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    query = takeCommand().lower()

    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        speak(results)
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    # elif "play songs" in query:
