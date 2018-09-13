#Created by Shikha Singh

import cv2

#Creating a function to generate live sketch of the object detected by webcam
def sketch(img):
    
    #The 'if' statement is used to check that frames are passed correctly
    if img is not None:
        print("image is present")
        print(len(img.shape))
        
    #converting the image to grayscale color space to apply thresholding
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #using blurring operation(Gaussian Blur) to smoothen & clean up any noise in the image
    img_gray_blur=cv2.GaussianBlur(img_gray,(3,3),0)
    
    #for edge detection, using 'Canny' method
    canny_edges=cv2.Canny(img_gray_blur,10,70)
    
    #the threshold operation returns 2 functions:
    #'ret' is a boolean variable returning True or False if the image is detected or not respectively
    #'mask' is our final sketch after applying all image manipulation functions
    ret,mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_TOZERO)
    return mask

#Creating a cap variable which pulls image from the webcam
cap=cv2.VideoCapture(1)

#running a loop, else the cap variable will capture image of a particular instant
while True:
    #'frame' refers to the actual image captured from the webcam
    ret,frame=cap.read()
    
    #applying an 'if' condition to check if captured image is detected in the program 
    if frame is not None:
        print("frame present")
        
    #the 'imshow' function is used for displaying the openCV window with the desired output
    cv2.imshow('live sketcher',sketch(frame))
    
    #waitKey() function allows to input an information when a window is open
    #applying condition for detection of enter key
    #thus, the program terminates when user presses Enter key
    if cv2.waitKey(1)==13:
        break
        
#cap.release() is used to release the camera. If it is not applied, leads to either abnormal termination or 
#hanging & locking up of the kernel.
cap.release()

#the below command is used to close all open windows of openCV
cv2.destroyAllWindows()
