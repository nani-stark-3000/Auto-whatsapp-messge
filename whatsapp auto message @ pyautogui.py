import pyautogui as pg
import time
import pywhatkit as pw
import datetime
import random

c_time= datetime.datetime.now()                 # store present time in a variable 
h = c_time.hour
m = c_time.minute+2                             # set minute to present time + 2

phone= '+91'+(input("Enter phone number to send message : "))       # phone number input

n=int(input("Enter no.of messages to be sent : "))

t=int(input("Enter delay time : "))

pw.sendwhatmsg(phone,'hello',h,m)           # Open whatsapp web and set cursor at require  contact page 

a=["Hello","Hi","Hey","Good Morning","Good Night","Good Evening","Good Afternoon"]
# list of messages

c = len(a)-1
for i in range(n):
    b = random.randint(0,c)         # Selecting a random index in list
    pg.typewrite(a[b])              # Typing text
    time.sleep(t)
    pg.press("enter")               # Enter to send
