
import cv2

img = cv2.imread('BART_cc_map.png',0)
cv2.imshow('BartMap',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print "hello_world"