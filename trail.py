from flask import Flask,render_template,request
import pyautogui as pg
import time
import datetime
import random
app = Flask(__name__)
@app.route('/vd', methods=['POST','GET'])
def index_home():
    if request.method==["POST","GET"]:
        phone = request.form.get('phone')
        n = request.form.get('count')
        t = request.form.get('delay')
        return render_template('new.html')
    return render_template('new.html')
app.run(debug=True,port=47)