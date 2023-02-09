import pyttsx3;
import datetime;
import speech_recognition as sr;
import wikipedia as wkpda

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour <12 :
    speak("Good Morning")
  elif hour>=12 and hour<18:
    speak("Good Afternoon")
  else:
    speak("Good Evening!")

  speak("Hello sir, I am your Artificial Assistant")


def takeCommand():
  # It take voice input from mic and returns string as output;

  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening>>>>")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognising")
    query = r.recognize_google(audio, language='en-in')
    print(f"User said : {query}")
  except Exception as e:
    print(e)
    print("Say again please........")
    return "None"

  return query


if __name__ == "__main__":
  wishMe()
  # logic for tasks from query

  while False:
    query =takeCommand().lower()
  
    if 'wikipedia' in query or 'wiki pedia' in query: 
      speak("Searching wikipedia...")
      query = query.replace("wikipedia", "")
      results = wkpda.summary(query, sentences=3)
      speak(f"According to wikipedia {results}")




