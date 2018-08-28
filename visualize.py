import cv2

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       # draw circle here (etc...)
       f = open('coords.txt', 'a')
       print('x = %d, y = %d'%(x, y))
       coords_to_write = str(x) + ', ' + str(y) + '\n'
       f.write(coords_to_write)
       f.close()

def print_times(file):
	font = cv2.FONT_HERSHEY_COMPLEX
	loc = (373, 581)
	font_scale = 0.5
	font_color = (0, 0, 0)
	line_type = 1
	
	lines = [tuple(int(i) for i in line.split(',')) for line in open(file)]
	for line in lines:
		print line
	cv2.putText(img, '12:30', loc, font, font_scale, font_color, line_type)


img = cv2.imread('BART_cc_map.png',1)
cv2.namedWindow('BartMap')
cv2.setMouseCallback('BartMap', on_mouse)
print_times('coords.txt')


while(1):
    cv2.imshow('BartMap',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()