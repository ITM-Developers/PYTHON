import cv2 as cv
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np

frame = cv.imread('fotos/cat2.jpg')
cv.rectangle(frame, (0,0), (250,250), (0,255,0), thickness=2)
cv.putText(frame, "Texto de pruba", (250,250), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=1)
cv.imshow('title', frame)
cv.waitKey(0)