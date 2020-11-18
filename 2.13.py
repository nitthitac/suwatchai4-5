import cv2
import matplotlib.pyplot as plt

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img1 = cv2.imread('D:/bookPic/resize_brocooli.jpg')
img2 = cv2.imread('D:/bookPic/mixVeggies.jpg')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT create()
kp1, des1 = sift.detectAndCompute(img1_gray, None)
kp2, des2 = sift.detectAndCompute(img2_gray, None)
bf = cv2.BFMatcher()
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda  x: x.distance)
matching results = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None, flags=2)
show_image(matching_result)
print('des1, des2, matches =', len(des1), len(des2), len(matches))
plt.show()