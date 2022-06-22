
import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
cv2.imshow('Orginal_Image',img)

# print(img.shape) #rows,col,channels in tuple
# print(img.size) #number of pixels
# print(img.dtype) #image datatype
b,g,r = cv2.split(img)
cv2.imshow("Model blue image",b)
cv2.imshow("Model green image",g)
cv2.imshow("Model red image",r)


img = cv2.merge((b,g,r))

cv2.waitKey(0)
cv2.destroyAllWindows()