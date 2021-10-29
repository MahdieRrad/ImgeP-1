import cv2

imge = cv2.imread('3.jpg',0)
img = cv2.resize(imge,(500,600))
imgH = cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("Men",imgH)
cv2.waitKey()