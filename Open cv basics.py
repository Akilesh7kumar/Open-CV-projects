import cv2
import numpy as np
img = cv2.imread("img.jpg")
#displaying image
cv2.imshow("Output",img)
cv2.waitKey(0)  #0 to make infinite delay
#Video 
cap = cv2.VideoCapture("vid.mp4")
while True:
    success,img = cap.read()#while loop is adde becoz video is seq of imgs
    cv2.imshow("Video",img)        
    if(cv2.waitKey(1) & 0xFF == ord('q')): #press q to pause the videoplayback
        break
    
# for web cam streaming
cap = cv2.VideoCapture(0)  #0 for default cam and 1 for other cams
cap.set(3,640) #3-height
cap.set(4,480)# 4 widht
cap.set(10,100)# 10 brightness

while True:
    success,img = cap.read()#while loop is adde becoz video is seq of imgs
    cv2.imshow("Video",img)        
    if(cv2.waitKey(1) & 0xFF == ord('q')): #press q to pause the videoplayback
        break
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image",imgGray)
cv2.waitKey(0)

imgblur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur image",imgblur)
cv2.waitKey(0)

imgcanny = cv2.Canny(img,100,100)
cv2.imshow("Canny image",imgcanny)
cv2.waitKey(0)

kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(imgcanny,kernel,iterations=1)
cv2.imshow("Dilation image",imgDilation)
cv2.waitKey(0)

imgeroded =cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow("eroded image",imgeroded)
cv2.waitKey(0)

#sizing and conventions
print(img.shape)

imgResize = cv2.resize(img,(300,500))  #wid,height
cv2.imshow("Resized image",imgResize)
cv2.waitKey(0)

imgCropped = img[0:200,200:500]   #here heigth and widht
cv2.imshow("Cropped image",imgCropped)
cv2.waitKey(10)
