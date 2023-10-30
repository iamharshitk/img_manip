import cv2 as cv
import numpy as np


def adjust_brcont():
    global adjusted_img
    adjusted_img=img_br+ brightness
    cv.imshow(winname3,adjusted_img)

def change_brightness(val):
    global brightness
    brightness=val/100
    adjust_brcont()

def adjust_brigthness(img):
    global winname3
    winname3="Adjust Brigthness"
    cv.namedWindow(winname3)
    global img_br
    img_br=np.float32(img/255)
    global brightness, max_brightness
    brightness=1
    max_brightness=100

    cv.imshow(winname3,img)
    
    cv.createTrackbar("Brightness", winname3, brightness, max_brightness, change_brightness)
    cv.waitKey(0)
   
  
