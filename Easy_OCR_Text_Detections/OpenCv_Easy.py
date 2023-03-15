import cv2
import easyocr
import os
import threading

cap = cv2.VideoCapture(0)

def toscan(x):
    print("here")
    reader  = easyocr.Reader(['en'])
    bound = reader.readtext(x)
    print(bound)

if __name__ == "__main__":
    while True:
        success, img = cap.read()
        toscan(img)       
        cv2.imshow("Output", img)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# def toscan(img,reader):
#     bound = reader.readtext(img)
#     print(bound)

# if __name__ == "__main__":
#     reader  = easyocr.Reader(['en'])

#     while True:
#         success, img = cap.read()

#         scan = threading.Thread(target=toscan,args=(img,reader))
#         scan.start()

#         cv2.imshow("Output", img)
#         if cv2.waitKey(1) & 0XFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()