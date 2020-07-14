
import cv2
import numpy as np 

cv2.namedWindow("Text")

img=np.zeros((512, 512, 3), np.uint8)

cv2.putText(img, "HELLO!", (100,200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,4,(255,0,0),2)
cv2.resizeWindow("Text",1920, 1080)
cv2.imshow("Text", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()






