import cv2 as cv

sImagePath = "fotos/cat2.jpg"
frame = cv.imread(sImagePath)
iFrameWidth  = frame.shape[1]
iFrameHeigth = frame.shape[0]


cv.namedWindow("FRAME ORIGINAL")
cv.moveWindow("FRAME ORIGINAL", 0,0)
cv.imshow('FRAME ORIGINAL',frame)

frameResized = cv.resize(frame, (200,200))
cv.namedWindow("FRAME RESIZED")
cv.moveWindow("FRAME RESIZED", 0, iFrameHeigth + 50)
cv.imshow('FRAME RESIZED',frameResized)

frameCropped = frame[ 0:200, 0:200]
cv.namedWindow("FRAME CROPPED")
cv.moveWindow("FRAME CROPPED", iFrameWidth, 0)
cv.imshow('FRAME CROPPED',frameCropped)

cv.waitKey(0)
cv.destroyAllWindows()