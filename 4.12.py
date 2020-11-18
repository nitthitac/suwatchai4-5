import cv2

brown_circle = cv2.imread('D:/bookPic/brownCircle.jpg')
brown_circle = cv2.resize(brown_circle, (500,500))
print(brown_circle.shape)
cv2.imshow('Original', brown_circle)
gp = [brown_circle]
for i in range(4) :
    Gaussian_p = cv2.pyrDown(gp[i])
    print(Gaussian_p.shape)
    # cv2.imshow(str(1), Gaussian_p)
    gp.append(Gaussian_p)
print()
gp2 = [gp[4]]
print(gp[4].shape)
for i in range(4,0,-1) :
    # size = (gp[i-1].shape[1], gp(i-1).shape[0])
    # Gaussian_p = cv2.pyrUp(gp[i]. dstsize=size)
    Gaussian_p = cv2.pyrUp(gp[i])
    print(Gaussian_p.shape)
    cv2.imshow(str(i), Gaussian_p)
    gp2.append(Gaussian_p)
cv2.waitKey(0)
cv2.destroyAllwindows()