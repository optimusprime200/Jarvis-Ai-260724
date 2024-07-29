import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
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
    if 'play' in command: #youtube cmd
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
# time cmd    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk("it's" + time)

#date cmd   
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A %B %d, %Y')
        print(date)
        talk(date)
    
    
#web commands    
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    
    elif 'open' in command:
        url = command.replace('open', '')
        webbrowser.open(url)
    
    
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    
    elif 'search' in command:
        search = command.replace('search', '')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.open(url)
    
    
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    
    elif 'how to' in command:
        how = command.replace('how to', '')
        url = 'https://www.youtube.com/results?search_query=' + how
        webbrowser.open(url)
    
    
    elif 'stop' in command:
        print('stopping the program')
        talk("stopping the program")
        return False

        
while True:
    if not run_alexa():
        break


    
