import cv2
import matplotlib.pyplot as plt

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img = cv2.imread('D:/bookPic/dice.jpg')
show_image(img, 'Input')
img gray = cv2.imread('D:/bookPic/dice.jpg', 0)
ret, thresh = cv2.threshold(img_gray, 0, 255,cv2.THRESH_BINARY+.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,255), 2)
show_image(img, 'contours')

#counting score on each dice
dice = []
dots = []
i = -1
for row in hierarchy:
    for h in row:
        i +=1
        if h[3] == -1: #external contours
            dice.append(1)
            dots.append(0)
        else:
            parent = h[3]
            if parent in dice:
                loc = dice.index(parent)
                dots[loc] = dots[loc]+1

print(dice)
print(dots)
plt.show()