import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape)
print(img.size)
print(img.dtype)#uint8
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# ROI of Image - Region of Interest
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# resize
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))
# Add
# dst = cv2.add(img,img2)

# Add_WeightedMethod
dst = cv2.addWeighted(img,.9,img2,.8,0)

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


