#from multiprocessing.connection import wait
#from re import S
#from django.template import engines
#from setuptools import Command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener =  sr.Recognizer()

engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = 'invalid command'
    try:
        with sr.Microphone() as source:
            print('listening..........')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)     
    except:
        pass 
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song =  command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =  datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'information' in command:
        person = command.replace('information', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry you are so annoying')
    elif 'are you single' in command:
        talk('Yes i am')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('please say it again')

while True:
    run_alexa()



