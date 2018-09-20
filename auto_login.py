import pyautogui
import cv2
from PIL import ImageGrab
import aircv as ac

# obj:3:login 2:password 1:id

img = ImageGrab.grab()
img.save('screen.png')

if __name__ == "__main__":
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

if pos3!=None:
    print (pos3['result'])


if pos2!=None:
    print (pos2['result'])


if pos1!=None:
    print (pos1['result'])
