import cv2

imge=cv2.imread('4.jpg',0)
imge=cv2.resize(imge, (500,500))

Width,Height=imge.shape

for i in range (Width):
    for j in range(Height):
        if 255>imge[i,j]>185:
            imge[i,j]=185
        elif 184>imge[i,j]>140:
            imge[i,j]=160
        elif 129>imge[i,j]>90:
            imge[i,j]=120
        else:
            imge[i,j]=10

cv2.imshow(' Wolf ',imge)
cv2.waitKey()