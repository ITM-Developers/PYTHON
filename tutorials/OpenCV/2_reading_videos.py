import cv2 as cv

# Ruta a Video o un int para usar la camara
video = cv.VideoCapture('videos/avance.mp4')
while True:
    isTrue, frame = video.read()
    cv.imshow('Titulo del Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()