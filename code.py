#Created by Shikha Singh

import cv2

#Creating a function to generate live sketch of the object detected by webcam
def sketch(img):
    
    #The 'if' statement is used to check that images are passed correctly
    if img is not None:
        print("image is present")
        print(len(img.shape))
    return img

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
cap.release()
cv2.destroyAllWindows()
