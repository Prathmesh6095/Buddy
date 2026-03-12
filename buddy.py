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
                
                if "open notepad" in self.query:
                    npath = "C:\\Windows\\notepad.exe"
                    os.startfile(npath)
                    speak("Done sir.")

                elif "close notepad" in self.query:
                    speak("Okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")
                    speak("Done sir.")

                elif "open microsoft word" in self.query:
                    speak("sure sir")
                    wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
                    os.startfile(wpath)
                    speak("Done sir.")

                elif "close microsoft word" in self.query:
                    speak("Okay sir, closing word")
                    os.system("taskkill /f /im WINWORD.exe")
                    speak("Done sir.")

                elif "open powerpoint" in self.query:
                    speak("sure sir")
                    wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                    os.startfile(wpath)
                    speak("Done sir.")

                elif "close powerpoint" in self.query:
                    speak("Okay sir, closing powerpoint")
                    os.system("taskkill /f /im POWERPNT.EXE")
                    speak("Done sir.")