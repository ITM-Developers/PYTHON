import cv2 as cv

def rescaleFrame(frame, scale=0.50):
    height = int(frame.shape[0] * scale)
    width  = int(frame.shape[1] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# Ruta a Video o un int para usar la camara
video = cv.VideoCapture('videos/avance.mp4')
while True:
    isTrue, frame = video.read()

    frame_scaled = rescaleFrame(frame)
    cv.imshow('Titulo del Video', frame_scaled)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()