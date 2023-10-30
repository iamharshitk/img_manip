import cv2 as cv

def change_blur(val):
    global blur
    blur=val*10
    if blur==0:
        cv.imshow(winname4, xyz)
    elif blur<=250:
        perform_operation((3,3))
    elif blur>250 and blur<500:
        perform_operation((5,5))
    elif blur>=500 and blur<750:
        perform_operation((7,7))
    elif blur>=750 and blur<=1000:
        perform_operation((9,9))

def perform_operation(kernel):
    global adjusted_img
    adjusted_img=cv.GaussianBlur(xyz, kernel, blur)
    cv.imshow(winname4,adjusted_img)
    key=cv.waitKey(0)
    if key==ord('s'):
        cv.imwrite("Blurred.jpg", adjusted_img)
        cv.destroyAllWindows()


def main_func(img):
    global xyz
    xyz=img
    global blur_initial, max_blur, winname4
    winname4="Blur Image"
    cv.namedWindow(winname4)
    
    blur_initial=0
    max_blur=100
    cv.createTrackbar("Blur", winname4, blur_initial, max_blur, change_blur)
    cv.imshow(winname4,img)
    cv.waitKey(0)
    cv.destroyAllWindows()

