import cv2
import numpy as np 


img=np.zeros((512, 512, 3), np.uint8)

cv2.circle(img, (200,200), (200), (0,0,255), -1)

cv2.putText(img, "HELLO!", (50,150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,4,(255,0,0),2)
cv2.imshow("Circle",img)

cv2.waitKey(1000)
cv2.destroyAllWindows()






