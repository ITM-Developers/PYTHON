import cv2 as cv

frame = cv.imread('fotos/cat2.jpg')
cv.imshow('window title', frame)
cv.waitKey(0)