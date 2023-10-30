import cv2 as cv
import numpy as np
import bright
import blurr
import splitc
import conv
import rem_bg

window="SR Task 1"
input_check=0

def tinput_img():
    global img, input_check
    img_path=input("Enter the path of the image:\n")
    img=cv.imread(img_path)
    input_check=1
    menu()

def input_img():
    global img, input_check
    img_path=input("Enter the path of the image:\n")
    img=cv.imread(img_path)
    input_check=1
   

def show_img():
    img_check()
    cv.imshow("Original Image", img)
    cv.waitKey(0)
    menu()
    

def img_check():
    if input_check==0:
        print("Error: No input image found\n")
        input_img()



def menu():
    print("1. Input an image")
    print("2. View the input image")
    print("3. Adjust image brightness")
    print("4. Adjust image contrast")
    print("5. Blur image")
    print("6. Split image channels")
    print("7. Convert image to different colour formats")
    print("8. Remove image background")
    print("9. Exit")

    task=int(input("Enter operation number:\n"))

    if task==1:
        tinput_img()

    elif task==2:
        img_check()
        show_img()

    elif task==3:
        img_check()
        bright.adjust_brigthness(img)
        menu()
    

    elif task==5:
       img_check()
       print("Press 's' to save the image")
       blurr.main_func(img)
       menu()

    elif task==6:
       img_check()
       print("Press 's' to save the image\n")
       splitc.operate(img)
       menu()

    elif task==7:
       img_check()
       print("Press 's' to save the image\n")
       conv.operate(img)
       menu()

    elif task==8:
        img_check()
        print("Press 's' to save the image\n")
        rem_bg.bgremove(img)
        menu()

    elif task==9:
        exit()

    else:
        print("Please enter a valid index")
        menu()


print("*********SR DTU TASK 1**********\n")
menu()





