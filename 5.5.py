import cv2
import matplotlib.pyplot as plt

def show_image(BGRimage, windowName=None):
    plt.figure(windowName)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2RGB)
    plt.imshow(RGBimage)

img = cv2.imread('D:/bookPic/block.jpg')
img gray = cv2.cvtColor(img. cv2.COLOR_BGR2GRAY)
show_image(img, 'Input')
result = cv2.goodFeaturesToTrack(img_gray, 4/2, 0.01, 10)
result = np.int0(result)
#draw a circle around the detected corners
for i in result:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)
show_image(img, 'Output')
plt.show()