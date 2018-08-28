import cv2
import math

in_file = 'coords.txt'
locations = [tuple(int(i) for i in line.split(',')) for line in open(in_file)]
img = cv2.imread('BART_cc_map.png',1)
cv2.namedWindow('BartMap')

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # draw circle here (etc...)
        print('x = %d, y = %d'%(x, y))
        locations.append((x, y))

cv2.setMouseCallback('BartMap', on_mouse)

def distance(list_tuple, click_tuple):
    x1 = list_tuple[0]
    x2 = click_tuple[0]
    y1 = list_tuple[1]
    y2 = click_tuple[1]

    return math.sqrt(((x2-x1)**2 + (y2-y1)**2))

def render():
    cv2.destroyAllWindows()
    global img
    img = cv2.imread('BART_cc_map.png',1)
    cv2.namedWindow('BartMap')
    cv2.imshow('BartMap',img)
    print_times()

def on_mouse_edit(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # draw circle here (etc...)
        min_distance = float('inf')
        closest_loc = 0
        for i in range(len(locations)):
            loc = locations[i]
            dist = distance(loc, (x,y))
            if dist < min_distance:
                min_distance = dist
                closest_loc = i
        locations[closest_loc] = (x, y)
        render()
        cv2.setMouseCallback('BartMap', on_mouse_edit)

def print_times():
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 0.5
    font_color = (0, 0, 0)
    line_type = 1

    for loc in locations:
        cv2.putText(img, '12:30', loc, font, font_scale, font_color, line_type)

def write_coords():
    f = open(in_file, 'w')
    for loc in locations:
        coords_to_write = str(loc[0]) + ', ' + str(loc[1]) + '\n'
        f.write(coords_to_write)
    f.close()


while(1):
    cv2.imshow('BartMap',img)
    print_times()
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    if k == 101:
        cv2.setMouseCallback('BartMap', on_mouse_edit)
    if k == 105:
        cv2.setMouseCallback('BartMap', on_mouse)

cv2.destroyAllWindows()
write_coords()
