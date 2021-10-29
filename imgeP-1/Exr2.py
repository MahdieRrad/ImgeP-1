import cv2

imgeE = cv2.imread('1.jpg',0)
imgeM =cv2.imread('2.jpg',0)
imgeE[:,:] = 255-imgeE[:,:]
imgeM[:,:] = 255-imgeM[:,:]

cv2.imshow('Emilia',imgeE)
cv2.imshow('Man',imgeM)

cv2.waitKey()