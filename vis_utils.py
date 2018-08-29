import cv2
import math
import requests
import json
from data import Data
from datetime import datetime
import time as Time

from SdsClient import SdsClient
from SdsStream import SdsStream

stations = {"12th" : (604, 375), "16th" : (0, 489), "19th" : (540, 350), "24th" : (0, 507), "ashb" : (250, 294), "antc" : (890, 23), "balb" : (0, 542), 
"bayf" : (616, 568), "cast" : (686, 626), "civc" : (0, 470), "cols" : (788, 503), "colm" : (84, 626), "conc" : (731, 166), "daly" : (50, 595), "dbrk" : (170, 271), "dubl" : (
909, 577), "deln" : (125, 194), "plza" : (160, 219), "embr" : (0, 419), "frmt" : (705, 844), "ftvl" : (545, 471), "glen" : (0, 522), "hayw" : (550, 687), "lafy" : (602, 247), "lake" : (534, 439), 
"mcar" : (255, 322), "mlbr" : (240, 795), "mont" : (0, 436), "nbrk" : (180, 245), "ncon" : (871, 139), "oakl" : (445, 647), "orin" : (548, 274), "pitt" : (888, 112), "pctr" : (909, 84), 
"phil" : (831, 194), "powl" : (0, 455), "rich" : (135, 143), "rock" : (516, 301), "sbrn" : (115, 690), "sfia" : (305, 695), "shay" : (580, 737), "ssan" : (60, 658), "ucty" : (640, 795), 
"warm" : (860, 926), "wcrk" : (673, 219), "wdub" : (798, 633), "woak" : (185, 384), "sanl" : (618, 535)}

station_arrive_times = {}

#Replace

client = SdsClient(tenantID, address, resource, Authority, clientId, clientSecret)


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
	return min_station


def get_last(station):
	try:
		last_val = client.getLastValue(namespaceId, station, Data)
		station_arrive_times[station] = last_val.ArriveTime
		return str(last_val.ArriveTime)
	except:
		station_arrive_times[station] = "No Data"
		return "No Data"

def get_fare(station):
	try: 
		last_val = client.getLastValue(namespaceId, station, Data)
		return str(last_val.Fare)
	except:
		return "No Data"