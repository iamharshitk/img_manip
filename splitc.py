import cv2 as cv
import numpy as np


def open_img(entered):
    if entered==1:
        bll=cv.merge([b,arr,arr])
        cv.imshow("Blue", bll)
        k=cv.waitKey(0)
        if k==ord('s'):
            cv.imwrite("Blue_Channel.jpg",bll)
            cv.destroyAllWindows()
    elif entered==2:
        grr=cv.merge([arr,g,arr])
        cv.imshow("Green", grr)
        k=cv.waitKey(0)
        if k==ord('s'):
            cv.imwrite("Green_Channel.jpg",grr)
            cv.destroyAllWindows()

    elif entered==3:
        ree=cv.merge([arr,arr,r])
        cv.imshow("Red", ree)
        k=cv.waitKey(0)
        if k==ord('s'):
            cv.imwrite("Red_Channel.jpg",ree)
            cv.destroyAllWindows()
    
   
def operate(img):

    global arr, b, g, r
    arr=np.ones(img.shape[:2],dtype="uint8")
    b,g,r=cv.split(img)

    x=int(input("Enter 1 to view Blue channel\nEnter 2 to view Green channel\nEnter 3 to view Red channel\n"))
    open_img(x)




