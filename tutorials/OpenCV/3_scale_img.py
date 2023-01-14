import cv2 as cv

def rescaleFrame(frame, scale=0.50):
    height = int(frame.shape[0] * scale)
    width  = int(frame.shape[1] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

frame = cv.imread('fotos/cat1.jpg')
frame_scaled = rescaleFrame(frame)

cv.imshow('window title', frame_scaled)
cv.waitKey(0)