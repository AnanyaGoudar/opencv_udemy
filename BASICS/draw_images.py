
import cv2
import numpy as np 

img=np.zeros((512, 512, 3), np.uint8)

imgBW=np.zeros((512, 512), np.uint8)

cv2.imshow("Black rectangle", img)
cv2.imshow("black rectangle(BW)", imgBW)

cv2.waitKey(3000)
cv2.destroyAllWindows()