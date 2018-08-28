import cv2
import vis_utils

img = cv2.imread('BART_cc_map.png',1)
cv2.namedWindow('BartMap')
cv2.setMouseCallback('BartMap', vis_utils.on_mouse)

###use this for updating times
def render():
    cv2.destroyAllWindows()
    global img
    img = cv2.imread('BART_cc_map.png',1)
    cv2.namedWindow('BartMap')
    cv2.imshow('BartMap',img)
    print_times()

def print_locations():
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.5
    font_color = (0, 0, 0)
    line_type = 1

    for key, value in vis_utils.stations.iteritems():
        cv2.putText(img, key, value, font, font_scale, font_color, line_type)

while(1):
    cv2.imshow('BartMap',img)
    print_locations()
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()