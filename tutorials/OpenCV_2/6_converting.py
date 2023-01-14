import cv2 as cv

sImagePath = "fotos/cat2.jpg"
frame = cv.imread(sImagePath)
iFrameWidth  = frame.shape[1]
iFrameHeigth = frame.shape[0]

cv.namedWindow("RGB")
cv.moveWindow("RGB", 0,0)
cv.imshow('RGB',frame)

grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
cv.namedWindow("GRAY")
cv.moveWindow("GRAY", iFrameWidth,0)
cv.imshow('GRAY',grayFrame)

blurFrame = cv.GaussianBlur(frame, (9,9), cv.BORDER_DEFAULT)
cv.namedWindow("BLUR")
cv.moveWindow("BLUR", 0, iFrameHeigth)
cv.imshow('BLUR',blurFrame)

cannyFrame = cv.Canny(frame, 125,175)
cv.namedWindow("CANNY")
cv.moveWindow("CANNY", iFrameWidth, iFrameHeigth)
cv.imshow('CANNY',cannyFrame)

cv.waitKey(0)
cv.destroyAllWindows()