import cv2 as cv
import numpy as np


def bgremove(myimage):
  
    myimage_hsv = cv.cvtColor(myimage, cv.COLOR_BGR2HSV)
     
    s = myimage_hsv[:,:,1]
    s = np.where(s < 127, 0, 1) 

    # We increase the brightness of the image and then mod by 255
    v = (myimage_hsv[:,:,2] + 127) % 255
    v = np.where(v > 127, 1, 0)  # Any value above 127 will be part of our mask
 
    # Combine our two masks based on S and V into a single "Foreground"
    foreground = np.where(s+v > 0, 1, 0).astype(np.uint8)  #Casting back into 8bit integer
 
    background = np.where(foreground==0,255,0).astype(np.uint8) # Invert foreground to get background in uint8
    background = cv.cvtColor(background, cv.COLOR_GRAY2BGR)  # Convert background back into BGR space
    foreground=cv.bitwise_and(myimage,myimage,mask=foreground) # Apply our foreground map to original image
    finalimage = background+foreground # Combine foreground and background
 
    cv.imshow("Output", finalimage)
    k=cv.waitKey(0)
    if k==ord('s'):
        cv.imwrite("bg_removed.png",finalimage)
        cv.destroyAllWindows()

