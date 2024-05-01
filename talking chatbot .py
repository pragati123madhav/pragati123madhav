
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning guys!")
    elif hour>=12 and hour<16:
        speak("good afternoon guys!")
    else:
        speak("good evening guys!")
    speak("hello i your chatbot friend, tell me how can i help you")
    print("here is the list of work i can do: 1:open youtube"

          "2:open google"
          "3:open bluestacks.com"
          "4:play music"
          "5:wikipedia"
          "6:the time"
          "7:email"
          "8:open code"
          "9:ask how are you or what's up"
          "10:bye to end working")

    speak(" the list of work i can do: 1:open youtube"
          "2:open google"
          "3:open bluestacks.com"
          "4:play music"
          "5:wikipedia"
          "6:the time"
          "7:email"
          "8:open code"
          "9: ask how are you or what's up"
          "10:bye to end working")


def takecommand():
    #it takes microphone input and returns string output
  r = sr.Recognizer()
  with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

  try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='eng-in')
        print(f"user said: {query}\n")

  except Exception as e:
    print(e)
    print("say that again please...")
    return "none"
  return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pragmadhav2003@gmail.com','your password')#your gmail and password should be there.
    server.sendmail('jenny.zira01@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open bluestacks.com' in query:
            webbrowser.open("bluestacks.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\sudha\Music\Video Projects'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"dear,the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(codepath)
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!''I am fine!''Nice!''I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email to harry' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "jenny.zira01@gmail.com"
                sendEmail(to,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("sorry my friend ,I am not able to send email")

        elif 'bye' in query:
            speak('Bye pragati, have a good day.')
            sys.exit()





