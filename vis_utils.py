import cv2
import math

stations = {"12th" : (604, 375), "16th" : (32, 489), "19th" : (540, 350), "24th" : (25, 507), "ashb" : (280, 294), "antc" : (890, 23), "balb" : (22, 542), 
"bayf" : (616, 568), "cast" : (686, 626), "civc" : (14, 470), "cols" : (788, 503), "colm" : (84, 626), "conc" : (731, 166), "daly" : (50, 595), "dbrk" : (199, 271), "dubl" : (
909, 577), "deln" : (159, 194), "plza" : (194, 219), "embr" : (102, 419), "frmt" : (717, 844), "ftvl" : (545, 471), "glen" : (43, 525), "hayw" : (559, 687), "lafy" : (602, 247), "lake" : (534, 439), 
"mcar" : (289, 322), "mlbr" : (251, 795), "mont" : (68, 436), "nbrk" : (210, 245), "ncon" : (871, 139), "oakl" : (453, 647), "orin" : (548, 274), "pitt" : (888, 112), "pctr" : (909, 84), 
"phil" : (831, 194), "powl" : (82, 455), "rich" : (153, 143), "rock" : (516, 301), "sbrn" : (134, 690), "sfia" : (320, 695), "shay" : (593, 737), "ssan" : (60, 658), "ucty" : (645, 795), 
"warm" : (879, 926), "wcrk" : (673, 219), "wdub" : (798, 633), "woak" : (218, 384), "sanl" : (618, 535)}

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('x = %d, y = %d'%(x, y))
        get_closest_station((x,y))

def distance(list_tuple, click_tuple):
    x1 = list_tuple[0]
    x2 = click_tuple[0]
    y1 = list_tuple[1]
    y2 = click_tuple[1]

    return math.sqrt(((x2-x1)**2 + (y2-y1)**2))

def get_closest_station(click_tuple):
	min_dist = float('inf')
	min_station = ""
	for key, value in stations.iteritems():
		cur_dist = distance(value, click_tuple)
		if (cur_dist < min_dist):
			min_dist = cur_dist
			min_station = key
	print min_station
