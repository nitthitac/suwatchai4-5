import cv2
import matplotlib.pyplot as plt

def show_gray(img, windowName=None):
    plt.figure(windowName)
    plt.imshow(img, cmap='gray')

def detect_face(gray, image):
    faces = face_casced.detectMultiScale(gray, 1.1, 6)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0),4)

def detect_eye(gray, image):
    faces = face_casced.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0),4)

face cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcasced_eye.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect_face(gray, frame)
    detect_eye(gray, frame)
    cv2.imshow,('Detection',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break;
cap.release()
cv2.destroyAllWindows()