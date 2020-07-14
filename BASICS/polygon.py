import cv2
import numpy as np 

cv2.namedWindow("polygon")
img=np.zeros((512, 512, 3), np.uint8)

pts=np.array([[10,150], [200,250], [300,350], [500, 450]], np.int32)

pts=pts.reshape((1,-1,2))

cv2.polylines(img, [pts], True, (255,0,0),2)
cv2.resizeWindow("polygon",1920, 1080)
cv2.imshow("polygon",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()