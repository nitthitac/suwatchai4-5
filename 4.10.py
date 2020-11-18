import cv2
import matplotlib.pyplot as plt

#a function to show BGR image on screen
def show_image(BGRimage, windowName=None) :
    img_RGB = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.figure(windowName)
    plt.imshow(img_RGB)

#a function to convert BGR to gray
def BGR2Gray(BGRimage) :
    return cv2.cvtColor (BGRimage, cv2.COLOR_BGR2RGBGRAY)

#a function to show gray image on screen
def show_gray(gray_img, windowName) :
    plt.figure(windowName)
    plt.imshow(gray_img, cmap='gray')

img = cv2.imread('D:/bookPic/pond.jpg')
text = cv2.imread('D:bookPic/holiday.jpg')
text_gray = BGR2Gray(text)
show_gray(text_gray, 'text_gray')
ret, mask = cv2.threshold(text_gray, 127, 255, cv2.THRESH_BINARY_INV)
show_gray(mask, 'mask')
foreground = cv2.bitwise_or(text, text, mask=mask)
show_image(foreground, 'Foreground')

x_offset = 0
y_offset = 0
roi = img[y_offset:y_offset+text.shape[0], x_offset:x_offset+text.shape[1]]
show_image(roi, 'ROI')
#black out all the foreground text area in the bacground image
roi[mask>0] = 0
show_image(roi, 'Final ROI')
roi = cv2.add(roi, foreground)
show_image(roi, 'Blended ROI')
img[y_offset:y_offset+text.shape[0], x_offset:x_offset+text.shape[1]] = roi
show_image(img, 'Output')
plt.show()