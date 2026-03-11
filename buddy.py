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