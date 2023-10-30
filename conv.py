import cv2 as cv



def perform(X):
    if x==1:
        changed=cv.cvtColor(op_img, cv.COLOR_BGR2HSV)
        cv.imshow("HSV", changed)
        k=cv.waitKey(0)
        if k==ord('s'):
            cv.imwrite("HSV.jpg", changed)
            cv.destroyAllWindows()

    elif x==2:
        changed=cv.cvtColor(op_img, cv.COLOR_BGR2RGB)
        cv.imshow("RGB", changed)
        k=cv.waitKey(0)
        if k==ord('s'):
            cv.imwrite("RGB.jpg", changed)
            cv.destroyAllWindows()

    if x==3:
        changed=cv.cvtColor(op_img, cv.COLOR_BGR2GRAY)
        cv.imshow("GRAYSCALE", changed)
        k=cv.waitKey(0)
        if k==ord('s'):
            cv.imwrite("GRAY.jpg", changed)
            cv.destroyAllWindows()
        

def operate(img):
    global op_img, x
    op_img=img
    x=int(input(" 1. HSV\n 2. RGB\n 3. Grayscale\n"))
    perform(x)

