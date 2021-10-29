#1-Safhe Shtrnge
import cv2
import numpy as NumPy

imge = NumPy.arange(0, 360000, 1, NumPy.uint8)
imge = NumPy.reshape(imge, (600, 600))
Width,Height = imge.shape

for i in range(0,Width,100):
    for j in range(0,Height,100):
        if ((i+j)/4)%2==0:
            imge[i:i+100,j:j+100]=0
        else:
            imge[i:i+100,j:j+100]=255

cv2.imshow('Checkered Page',imge)
cv2.waitKey()