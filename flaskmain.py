from flask import Flask,render_template,request
import pyautogui as pg
import time
import pywhatkit as pw
import datetime
import random
app = Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index_home():
    if request.method==["POST","GET"]:
        c_time= datetime.datetime.now()             
        h = c_time.hour
        m = c_time.minute+2  
        phone = request.form.get('phone')
        n = request.form.get('count')
        t = request.form.get('delay')
        pw.sendwhatmsg(phone,'hello',h,m)           
        a=["Hello","Hi","Hey","Good Morning","Good Night","Good Evening","Good Afternoon"]
        c = len(a)-1
        for i in range(n):
            b = random.randint(0,c)         # Selecting a random index in list
            pg.typewrite(a[b])              # Typing text
            time.sleep(t)
            pg.press("enter")
    return render_template('new.html')
app.run(debug=True,port=34)
