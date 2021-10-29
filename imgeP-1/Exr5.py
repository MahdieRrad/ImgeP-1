import cv2

imge = cv2.imread('5.jpg',0)
imge = cv2.resize(imge,(650,500))
cv2.line(imge,(-5,150),
             (150,-5),
             (10,10,10),25)
cv2.imshow('TonyStrak Dead',imge)
cv2.waitKey()