import cv2
from PIL import Image
import pytesseract
import threading

cap = cv2.VideoCapture(0)

def tesseract_read_image():
    OCR = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    ImagePath = r'C:/Users/jlukas/Desktop/My_Projects/to_upload/Character_Detections/Tesseract_OCR_Text_Detections/test1.jpg'
    pytesseract.pytesseract.tesseract_cmd = OCR

    img = cv2.imread(ImagePath)
    img = cv2.resize(img, (400, 450))
    #cv2.imshow("Output",img)
    text=pytesseract.image_to_string(img)
    print(text)
#tesseract_read_image()

def tesseract_stream_video():
    OCR = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = OCR
    #cv2.imshow("Output",img)
    text=pytesseract.image_to_string(img)
    print(text)
#tesseract_stream_video()

while True:
    global img
    saved_path = r'C:/Users/jlukas/Desktop/My_Projects/to_upload/Character_Detections/Tesseract_OCR_Text_Detections/'
    success, img = cap.read()    
    tesseract_stream_video() # or use global img
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0XFF == ord('s'):
        #cv2.imwrite(saved_path + 'test1.jpg',img)
        break
cap.release()
cv2.destroyAllWindows()

