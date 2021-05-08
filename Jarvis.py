import pyttsx3
from tkinter import *
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import webbrowser
import wikipedia
import smtplib
import sys
import pyautogui
import datetime
import instaloader
import time
import PyPDF2
import requests
from tkinter import *
from tkinter import *
from PIL import Image,ImageTk
from pyjokes import *
from sys import *
from PyDictionary import *
from psutil import *
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import os
import getpass
import operator






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0],id)
engine.setProperty('voices',voices[0].id)

def gui():
    window = Tk()
    window.title('Grand Canyon')
    canvas = Canvas(window, width = 500, height = 500)
    canvas.pack()
    my_image = PhotoImage(file='ironman.gif')
    canvas.create_image(0, 0, anchor = NW, image=my_image)
    window.mainloop()
def speak(audio):
            engine.say(audio)
            print(audio)
            engine.runAndWait()

def takecommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening")
                r.pause_threshold = 1
                audio = r.listen(source,timeout=100,phrase_time_limit=100)

            try:
                print("Recognizing........")
                query= r.recognize_google(audio,language='en-in')
                print(f"user said:{query}")
            except Exception as e:
                speak("Please say that again")
                return "none"
            return query



def Wishme():
        hour = datetime.datetime.now().hour
        
        if hour >=0 and hour <=12:
            speak("Good Morning Sir")
        elif hour>12 and hour<18:
            speak("Good Evening Sir")
        else:
            speak("Good Night Sir")
            speak("I am JARVIS sir Please tell me how can i serve you")

def pdfreader():
        book = open("oop.dff",'rb')
        reader= PyPDF2.PdfFileReader(book)
        pages = reader.numPages
        speak("the number of pages in the provided pdf file are{pages}")
        pg=int(input("Enter the page number of this pdf file you want to listen:"))
        page=reader.getPage(pg)
        text=page.extractText()
        speak(text)
        print(text)
        

def sendEmail(to,content):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login('thechangemaker45@gmail.com', 'changemaker')
        server.sendmail('mehraj9622873166@gmail.com',to,content)
        server.close()
    
def cpu():
        usage = str(psutil.cpu_percent())
        speak("CPU is at"+usage)

        battery = psutil.sensors_battery()
        speak("battery is at")
        speak(battery.percent)


def joke():
        for i in range(5):
            speak(pyjokes.get_jokes()[i])



    


def taskexecution():


    gui()
    if __name__ == "__main__": 
        Wishme()
        while True:
            query = takecommand().lower()

            #logic building

            if 'open notepad' in query:
                path = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(path)
            elif 'open command prompt' in query:
                os.system("start cmd")
            elif 'open VLC Media Player' in query:
                npath="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
                os.startfile(npath)
            elif 'open code' in query:
                mpath="C:\\Users\\Personal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(mpath)
            elif 'open camera' in query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()
            elif 'play music' in query:
                music_dir = "C:\\Users\\Public\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,song))



            elif 'open Flappy Bird' in query:
                zpath="C:\\Users\Personal\\Desktop\\PYTHON\\Python Projects\\Resources\\Car Aminated\\gallery\\Flappy Bird By sahil.py"
                os.startfile(zpath)

            elif 'open google chrome' in query:
                wpath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(wpath)
            elif 'open codeblocks' in query:
                cpath="C:\\Program Files\\CodeBlocks\\codeblocks.exe"
                os.startfile(wpath)    
            elif 'hide all files in the mentioned folder' in query or 'make the files visible in the mentioned folder' in query:
                speak('sir please tell me whether i have to hide the files or make it visible')
                cond = takecommand().lower()
                if 'hide' in cond:
                    os.system("attrib +b /s/d")
                    speak("all the files are successfully hidden sir")
                
                elif 'visible' in cond:
                    os.system("attrib -h /s /d")
                    speak("sir all the files are visible now")
                elif "leave it" in cond:
                    speak("ok sir")
            
            elif 'who am i' in query:
                speak("Sir you are Sahil Mehraj,you are my Master you created me")
            elif 'who Created You' in query:
                speak("i was created by My master Mister Sahil Mehraj")
            elif 'what can you do' in query:
                speak("I can perform mnay tasks like opening system softwares,informing you about weather and time and can even make you laugh by jokes")
            
            
            elif 'record video' in query:
                cap = cv2.VideoCapture(0)
                out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if ret:
                        
                        out.write(frame)

                        cv2.imshow('frame',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    else:
                        break
                cap.release()
                out.release()
                cv2.destroyAllWindows()
            elif "wikipedia" in query:
                speak("searching wikipedia")
                query = query.replace('wikipedia',"")
                results = wikipedia.summary(query, sentences=7)
                speak("According to wikipedia")
                speak(results)
                print(results)
            
            elif 'open youtube' in query:
                webbrowser.open("www.youtube.com")
            elif 'open rexdl' in query:
                webbrowser.open("www.rexdl.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("www.stackoverflow.com ")
            elif 'open google' in query:
                speak("sir, what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")
            
            elif 'email to me' in query:
                try:
                    speak("What should i say")
                    content= takecommand().lower()
                    to = "thechangemaker45@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent successfully")
                except Exception as e:
                    print(e)
                    speak("Email could not be sent due to some error")
            elif 'no thanks' in query:
                speak("Thank you for using me sir Have a good day")
                sys.exit()
            
            elif 'where am i' in query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.orf')
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requestes = requests.get(url)
                    geo_data=geo_requestes.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak("sir i am not sure but we think we are in {city} city of {country} country")
                except Exception as e:
                    speak("i was not able to find where we currently are because of network issue")
                    pass
            elif 'instagram profile' in query or 'profile on instagram' in query:
                speak("Sir please enter the user name correctly")
                name=input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                time.sleep(5)
                speak("sir would you like to down the profile of this account")
                condition = takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak ("i am done sir the profile picture is saved in our main folder, now i am ready to perform my next task")
                else:
                    pass
            elif 'read pdf book' in query:
                pdfreader()
                speak("sir the book is over now hope you liked it")
                speak("do you have any other work from me")
            elif 'exit' in query:
                quit()
            elif 'youtube downloader' in query:
                exec(open('youtube_downloader.py').read())

            elif 'voice' in query:
                speak("do i have to switch it to female")
                voice=takecommand()
                if 'female' in voice:
                    engine.setProperty('voice', voices[1].id)
                else:
                    engine.setProperty('voice', voices[0].id)
                speak("Hello Sir, I have switched my voice. How is it?")
            

           


            elif 'tell me the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f'Sir, the time is {strTime}')

            elif 'i want to make a google search' in query:
                speak('What do you want to search for?')
                search = takecommand().lower()
                url = 'https://google.com/search?q=' + search
                webbrowser.get('chrome').open_new_tab(
                    url)
                speak('Here is What I found for' + search)

            elif 'location' in query:
                speak('What is the location?')
                location = takecommand().lower
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get('chrome').open_new_tab(url)
                speak('Here is the location ' + location)
            

            elif 'remember that' in query:
                speak("what should i remember sir")
                rememberMessage = takecommand().lower()
                speak("you said me to remember"+rememberMessage)
                remember = open('data.txt', 'w')
                remember.write(rememberMessage)
                remember.close()

            elif 'do you remember anything' in query:
                remember = open('data.txt', 'r')
                speak("you said me to remember that" + remember.read())

            elif 'sleep' in query:
                sys.exit()


            elif ' tell me the latest news' in query:
                speak('Ofcourse sir..')
                speak_news()
                speak('Do you want to read the full news...')
                test = takecommand().lower
                if 'yes' in test:
                    speak('Ok Sir, Opening browser...')
                    webbrowser.open(getNewsUrl())
                    speak('You can now read the full news from this website.')
                else:
                    speak('No Problem Sir')
            
            elif 'shutdown' in query:
                if platform == "win32":
                    os.system('shutdown /p /f')
                elif platform == "linux" or platform == "linux2" or "darwin":
                    os.system('poweroff')

            elif 'tell me about my cpu' in query:
                cpu()


            elif 'tell me a joke' in query:
                joke()
            
            elif 'do some calculation' in query or 'can ypu calculate' in query:
                r= sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What do u want to calculate, like example 3 plus 3 or 5 minus 3")
                    print("listening.......")
                    r.adjust_for_ambient_noise(source)
                    audio=r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {

                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1,oper,op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))


   
        

            

                
while True:
    permission=takecommand()
    if 'wake up' in permission:
        taskexecution()
    elif 'goodbye' in permission:
        speak("Thanks for using me sir good bye")
        quit()



