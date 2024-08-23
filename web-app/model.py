import pytesseract
import cv2
from matplotlib import pyplot as plt
# import os

def RecognizeText(image_path):
    image = cv2.imread(image_path)
    base_image = image.copy()
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
    dilate = cv2.dilate(thresh, kernel, iterations=1)
    
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
    
    results = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if h > 200 and w > 20:
            roi = image[y:y+h, x:x+w]
            cv2.rectangle(image, (x, y), (x+w, y+h), (38, 255, 12), 2)
            ocr_res = pytesseract.image_to_string(roi)
            ocr_res = ocr_res.split("\n")
            for i in ocr_res:
                results.append(i)
    
    names = []
    for i in results:
        i = i.strip().replace("\n", "")
        i = i.split(" ")[0]
        if len(i) > 2:
            try:
                i = int(i[0])
            except ValueError:
                names.append(''.join(huruf for huruf in i if huruf.isalnum()))
                
    return sorted(names)