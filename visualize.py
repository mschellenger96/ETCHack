import cv2
import vis_utils
import time
import random

img = cv2.imread('BART_cc_map.png',1)
cv2.namedWindow('BartMap')
cv2.setMouseCallback('BartMap', vis_utils.on_mouse)

###use this for updating times
def render():
    global img
    img = cv2.imread('BART_cc_map.png',1)
    cv2.namedWindow('BartMap')
    print_locations()
    cv2.imshow('BartMap',img)

def print_locations():
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.5
    font_color = (0, 0, 0)
    line_type = 1
    for key, value in vis_utils.stations.iteritems():
        cv2.putText(img, str(random.randint(1, 20)), value, font, font_scale, font_color, line_type)

while(1):
    render()
    
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    time.sleep(10)

cv2.destroyAllWindows()