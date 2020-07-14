import cv2
import numpy as np 

img=np.zeros((512, 512, 3),np.uint8)
cv2.rectangle(img, (150,200), (400, 350), (255, 0, 0),-1)
cv2.imshow("rectangle",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()