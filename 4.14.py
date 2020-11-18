import cv2
import  numpy as np

blue_c = cv2.imread('D:/bookPic/blueCircle.jpg')
brown_c = cv2.imread('D:/bookPic/brownCircle.jpg')
blue_c = cv2.resize(blue_c, (1000,1000))
brown_c = cv2.resize(brown_c, (1000,1000))
blue_brown = np.hstack((blue_c[:,:500], brown_c[:,500:1001]))
cv2.imshow('stack', blue_brown)
#1.create Gaussian pyramid for blue circle
gp_bl = [blue_c]
for i in range (6) :
    Gaussian = cv2.pyrDown(gp_bl[i])
    gp_bl.append(Gaussian)
#2.create Gaussian pyramid for brown circle
gp_bl = [brown_c]
for i in range (6) :
    Gaussian = cv2.pyrDown(gp_br[i])
    gp_br.append(Gaussian)
#3.Lapacian pyramid for blue circle
lp_bl = [gp_bl[6]]
for i in range (6,0,-1)
    size = (gp_bl[i-1].shape[1], gp_bl[i-1].shape[0])
    extended_Gaussian = cv2.pyrUp(gp_bl[i], dstsize=size)
    lapacian = cv2.subtract(gp_bl[i-1], extended_Gaussian)
    lp_bl.append(lapacian)
#4.Lapacian pyramid for brown circle
lp_bl = [gp_br[6]]
for i in range (6,0,-1)
    size = (gp_br[i-1].shape[1], gp_br[i-1].shape[0])
    extended_Gaussian = cv2.pyrUp(gp_br[i], dstsize=size)
    lapacian = cv2.subtract(gp_br[i-1], extended_Gaussian)
    lp_br.append(lapacian)

#5.combine the blue and brown lapacian pyramid
combined_lp=[]
n = 0
for blue, brown in zip(lp_bl, lp_br) :
    n = n+1
    w = int(blue.shape[0]/2)
    combined = np.hstack((blue[:,:w], brown[:,:w]))
    combined_lp.append(combined)
    #cv2.imshow(str(n), combined)
#6.Image reconstruction
combined_ball = combined_lp[0]
for i in range (l,len(combined_lp)):
    size = (combined_lp[i].shape[0], combined_lp[i].shape[1])
    combined_ball = cv2.pyrUp(combined_ball, dstsize=size)
    combined_ball = cv2.add(combined_lp[i], combined_ball)
    cv2.imshow(str(i), combined_ball)
cv2.waitKey(0)
cv2.destroyAllWindow()