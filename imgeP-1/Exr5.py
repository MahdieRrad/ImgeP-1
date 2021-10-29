import cv2

imge = cv2.imread('5.jpg',0)
imge = cv2.resize(imge,(500,500))
cv2.line(imge,(-5,150),(150,-5),(10,10,10),20)
cv2.imshow('TonyStark Dead',imge)
cv2.waitKey()
