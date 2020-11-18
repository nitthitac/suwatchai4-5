import cv2

brown_circle = cv2.imread('D:/bookPic/brownCircle.jpg')
brown_circle = cv2.resize(brown_circle, (500,500))
print(brown_circle.shape)
cv2.imshow('Original', brown_circle)
gp = [brown_circle]
for i in range(4) :
    Gaussian_p = cv2.pyrDown(gp[i])
    gp.append(Gaussian_p)
ip = [gp[4]]
for i in range(4,0,-1) :
    size = (gp[i-1].shape, gp[i-1].shape[0])
    extened_g = cv2.pyrUp(gp[i], dstsize=size)
    difference = cv2.subtract(gp[i-1], extened_g)
    cv2.imshow(str(i), difference)
    lp.append(difference)
cv2.waitKey(0)
cv2.destroyAllWindows()