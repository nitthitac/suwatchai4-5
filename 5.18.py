import cv2
import matplotlib.pyplot as plt

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

face cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcasced_eye.xml')
img1 = cv2.imread('D:/bookPic/rada_face.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('D:/bookPic/sideFace.jpg')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def detect_face(gray, image):
    faces = face_casced.detectMultiScale(gray, 1.1, 6)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0),4)

def detect_eye(gray, image):
    faces = face_casced.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0),4)


detect_face(gray1, img1)
detect_eye(gray1,img1)
show_image(img1, 'Detection')
plt.show()