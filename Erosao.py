import cv2 
import numpy as np 
 
img = cv2.imread('images.png', 0) 

kernel = np.ones((5,5), np.uint8) 

erosao = cv2.erode(img, kernel, iterations=1) 
  
cv2.imshow('Imagem Original', img) 
cv2.imshow('Erosao', erosao) 

cv2.waitKey(0) 