# import classifier

# classifier.organizeByMIME(
#     "/home/byron/Desktop/Workspace/PY/document-classification-system/input/",
#     "/home/byron/Desktop/Workspace/PY/document-classification-system/output/")


from PIL import Image
from pytesseract import pytesseract

print(pytesseract.image_to_string(Image.open('input/smart.jpg')))
