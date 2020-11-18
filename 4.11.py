import cv2

ิbrown_circle = cv2.imread('D:/bookPIC/brownCircle.jpg)
ิbrown_circle = cv2.resize(brown_circle, (500,500))
print(brown_circle.shape)
cv2.imshow('0', brown_circle)
gp = [brown_circle]
for i in range (4) :
    gaussian_p = cv2.pyrDown (gp[i])
    print(gaussian_p.shape)
    cv2.imshow(str(i), gaussian_p)
    gp.append (gaussian)
cv2.waitKey(0)
cv2.destroyAllWindow()