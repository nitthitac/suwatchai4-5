import cv2
import matplotlib.pyplot as plt

def show_image(BGRimage, windowName) :
    img_RGB = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.figure(windowName)
    plt.imshow(img_RGB)

img = cv2.imread('D:/bookPic/pond.jpg')
show_image(img, 'Original')
text = cv2.imread('D:bookPic/holiday.jpg')
show_image(text, 'TEXT')
#stick one image over another image
x_offset = 0
y_offset = 0
img[y_offset:y_offset+text.shape[0], x_offset:x_offset+text.shape[1]] = text
show_image(img, 'Output')
plt.show()