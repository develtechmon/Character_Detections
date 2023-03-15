import cv2
from PIL import Image
import pytesseract
import threading

cap = cv2.VideoCapture(0)

def tesseract_stream_video(img):
    OCR = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = OCR
    #cv2.imshow("Output",img)
    text=pytesseract.image_to_string(img)
    print(text)

if __name__ == "__main__":
    while True:
        success, img = cap.read()
        # scan = threading.Thread(target=tesseract_stream_video,args=(img,))
        # scan.start()   
        tesseract_stream_video(img)
        cv2.imshow("Output", img)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()