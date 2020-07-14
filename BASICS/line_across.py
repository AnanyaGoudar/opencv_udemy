import cv2
import numpy as np 

image=np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511, 511), (255, 127, 0), 1)
img=cv2.transpose(image)

cv2.imshow("Line",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()