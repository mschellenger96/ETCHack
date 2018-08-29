import cv2
import vis_utils
import time

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        station = vis_utils.get_closest_station((x,y))
        fare = vis_utils.get_fare(station)
        font = cv2.FONT_HERSHEY_COMPLEX
        font_scale = 0.5
        font_color = (0, 0, 0)
        line_type = 1

        print "fare: ", fare
        render(False)
        cv2.putText(img, '$' + fare, (450, 112), font, font_scale, font_color, line_type)
        cv2.imshow('BartMap',img)

img = cv2.imread('BART_cc_map.png',1)
cv2.namedWindow('BartMap')
cv2.setMouseCallback('BartMap', on_mouse)

###use this for updating times
def render(isRefrest):
    global img
    img = cv2.imread('BART_cc_map.png',1)
    cv2.namedWindow('BartMap')
    if isRefrest:
        put_text()
    else:
        put_cached_times()
    
    cv2.imshow('BartMap',img)

def put_text():
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.5
    font_color = (0, 0, 0)
    line_type = 1
    global img
    for key, value in vis_utils.stations.iteritems():   
        cv2.putText(img, vis_utils.get_last(key), value, font, font_scale, font_color, line_type)
    cv2.putText(img, "Fare: ", (400, 112), font, font_scale, font_color, line_type)

def put_cached_times():
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.5
    font_color = (0, 0, 0)
    line_type = 1
    global img
    for key, value in vis_utils.stations.iteritems():   
        cv2.putText(img, vis_utils.station_arrive_times[key], value, font, font_scale, font_color, line_type)
    cv2.putText(img, "Fare: ", (400, 112), font, font_scale, font_color, line_type)
    
render(True)

now = time.time()
future = now + 60

while(1):
    if time.time() > future:
        render(True)
        future = time.time() + 60
    
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()