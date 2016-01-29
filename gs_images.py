import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('thats-me.jpg', 0)
logo = cv2.imread('roi.jpg', 0)

print("shape")
print(img.shape)
print(logo.shape)

img = cv2.resize(img, (450, 280))

print(img.shape)

newImg = cv2.addWeighted(img, 0.7, logo, 0.3, 0)

cv2.imshow('newImg', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(newimg)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()