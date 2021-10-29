import cv2

image = cv2.imread('3.jpg',0)
Rimge = cv2.resize(image,(500,500))
Rimge = Rimge[500::-1,500::-1]
cv2.imshow('Men',Rimge)
cv2.waitKey()
