import pyautogui
import cv2
from PIL import ImageGrab
import aircv as ac
import time
import datetime
import random


#position

# obj:3:login 2:password 1:id

img = ImageGrab.grab()
img.save('screen.png')

def current__time():
    current_time=time.localtime(time.time())
    current_hours=current_time.tm_hour
    h=current_hours
    current_mins=current_time.tm_min
    m=current_mins
    current_secs=current_time.tm_sec
    s=current_secs

    year=current_time.tm_year
    mon=current_time.tm_mon
    mday=current_time.tm_mday

    random_min=random.uniform(-10,15)
    random_sec=random.uniform(0,59)

    mins=30+random_min
    secs=random_sec

    starttime=datetime.datetime(year,mon,mday,8,mins,secs,0)

    return starttime



def startrun():
    imsrc = ac.imread('screen.png')
    imobj3 = ac.imread('login_logo.png')
    imobj1 = ac.imread('employee_id.png')
    if ac.find_template(imsrc, imobj1)==None:
        imobj1 = ac.imread('employee_id_2.png')
    imobj2 = ac.imread('password.png')
    if ac.find_template(imsrc, imobj2)==None:
        imobj2 = ac.imread('password_2.png')


    # find the match position
    pos3 = ac.find_template(imsrc, imobj3)
    pos2 = ac.find_template(imsrc, imobj2)
    pos1 = ac.find_template(imsrc, imobj1)

    

#    if pos3!=None:
#       print (pos3['result'])


if __name__ == "__main__":
    startTime=current__time()
    while datetime.datetime.now() < startTime:
        time.sleep(1)
        startTime=current__time()
        

