import pyttsx3
import datetime
from time import sleep
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib 
import sys
import time
import pyjokes
import instaloader
import pyautogui
import PyPDF2
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import instaloader
import operator
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from buddyui import Ui_Dialog


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wishme():
    hour = int(datetime.datetime.now().hour)
    pt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good morning sir!, its {pt}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon sir!, its {pt}")

    else:
        speak(f"Good evening sir!, its {pt}")
    speak("I am Buddy , How can I help you?")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prathameshhatkar07@gmail.com','tkne adgo kwnp jwbt')
    server.sendmail('prathameshhatkar07@gmail.com',to,content)
    server.close()

def pdf_reader():
    pdf = open('Resume.pdf','rb')
    pdfreader = PyPDF2.PdfFileReader(pdf)
    pages = pdfreader.numPages
    speak(f"Total numbers of pages in this pdf are {pages}")
    speak("sir please enter the number of page i have to read.")
    pg = int(input("Please enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

        #Multi-threading
        def run(self):
            self.TaskExecution
        def takecommand(self):
#it takes microphone input from input and returns strring output
            r = sr.Recognizer()
            with sr.Microphone() as source:
                 print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio,language='en-in')
                print(f"User said:{query}")

            except Exception as e:
                #print(e)
                print("Say that again please...")
                return "None"
            query = query.lower()
            return query

#start function
        def TaskExecution(self):
            wishme()

            while True:
            #if 1:

                self.query = self.takecommand()

                #logic building for task
        #----------To perform specific tasks----------#
                
                if "open notepad" in self.query or "open the notepad" in self.query:
                    npath = "C:\\Windows\\notepad.exe"
                    os.startfile(npath)
                    speak("Done sir.")

                elif "close notepad" in self.query or "close notepad" in self.query:
                    speak("Okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                    speak("Done sir.")

                elif "open microsoft word" in self.query:
                    speak("sure sir")
                    wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
                    os.startfile(wpath)
                    speak("Done sir.")

                elif "close microsoft word" in self.query or "close the microsoft word " in self.query:
                    speak("Okay sir, closing word")
                    os.system("taskkill /f /im WINWORD.exe")
                    speak("Done sir.")

                elif "open powerpoint" in self.query:
                    speak("sure sir")
                    wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                    os.startfile(wpath)
                    speak("Done sir.")

                elif "close powerpoint" in self.query or "close the powerpoint" in self.query:
                    speak("Okay sir, closing powerpoint")
                    os.system("taskkill /f /im POWERPNT.EXE")
                    speak("Done sir.")

                elif "open excel" in self.query or "open the excel" in self.query:
                    speak("sure sir, opening excel")
                    wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(wpath)
                    speak("Done sir.")

                elif "close excel" in self.query or "close the excel " in self.query:
                    speak("Okay sir, closing excel")
                    os.system("taskkill /f /im EXCELS.EXE")
                    speak("Done sir.")

                elif "take screenshot" in self.query or "take a screenshot " in self.query or "take a screenshot" in self.query:
                    speak("sir,please tell me the name for this screenshot file.")
                    name = takecommand().lower()
                    speak("please sir hold the screen for few seconds, i am taking screenshot")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir, the screenshot has been saved in our main folder.")

                elif "open command prompt " in self.query or "open command prompt" in self.query:
                    os.system('start cmd')
                    speak("Done sir.")

                elif "open camera " in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam',img)
                        k = cv2.waitKey(50)
                        if k==27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()
                    speak("Done sir.")

                elif "close camera " in self.query or "close the camera " in self.query:
                    pyautogui.press("Esc")
                    time.sleep(1)
                    speak("Done sir.")

                elif "play music " in self.query or "play the music " in self.query:
                    music_dir = "D:\\music"
                    songs = os.listdir(music_dir)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(music_dir, rd))
                    speak("Done sir.")

                elif "tell me a joke " in self.query or "tell me the joke " in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "my ip address " in self.query or "ip address " in self.query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your IP address is {ip}")

                elif "wikipedia" in self.query:
                    speak("Searching wikipedia....")
                    self.query = self.query.replace("wikipedia","")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("According to wikipedia")
                    speak(results)

         #----------To check socialmedia----------#
                
                elif "open facebook" in self.query:
                    webbrowser.open("www.facebook.com")
                    speak("Done sir..")

                elif "open youtube" in self.query:
                    speak("Sir what would you like to see?")
                    yt = takecommand().lower()
                    kit.playonyt(f"{yt}")
                    speak("Done sir.")

                elif "open google" in self.query:
                    speak("Sir, what would you like to search?")
                    cm = takecommand().lower()
                    webbrowser.open(f"{cm}")
                    speak("Done sir...")

                elif "open chrome" in self.query:
                    speak("opening sir...")
                    apath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(apath)
                    speak("Done sir...")

                elif "close chrome" in self.query:
                    speak("Okay sir, closing chrome..")
                    os.system("taskkill /f /im chrome.exe")
                    speak("Done sir..")

                elif "switch the window " in self.query or "switch window " in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")