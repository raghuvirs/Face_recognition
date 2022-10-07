import cv2 as cv
img = cv.imread('12.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
har_cascade = cv.CascadeClassifier('harr_face.xml')
harcascade = har_cascade.dete
cv.waitKey(0)