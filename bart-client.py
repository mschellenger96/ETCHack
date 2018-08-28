import requests
import json
from data import Data
from datetime import datetime
import time as Time

from SdsClient import SdsClient
from SdsStream import SdsStream

base = "http://api.bart.gov/api/sched.aspx?cmd=depart&orig=SANL&dest={0}&date=now&key=MW9S-E7SL-26DU-VV8V&b=0&a=1&l=1&json=y"
stations = ["12th", "16th", "19th", "24th", "ashb", "antc", "balb", 
"bayf", "cast", "civc", "cols", "colm", "conc", "daly", "dbrk", "dubl", 
"deln", "plza", "embr", "frmt", "ftvl", "glen", "hayw", "lafy", "lake", 
"mcar", "mlbr", "mont", "nbrk", "ncon", "oakl", "orin", "pitt", "pctr", 
"phil", "powl", "rich", "rock", "sbrn", "sfia", "shay", "ssan", "ucty", 
"warm", "wcrk", "wdub", "woak"]

tenantID = "REPLACE"
namespaceId = "REPLACE"
clientId = "REPLACE"
clientSecret = "REPLACE"
resource = "REPLACE"
address = "REPLACE"
Authority = "REPLACE"

client = SdsClient(tenantID, address, resource, Authority, clientId, clientSecret)

while(True):
    time = str(datetime.utcnow())
    for station in stations:
        r = requests.get(base.format(station))
        j = r.json()
        trip = j["root"]["schedule"]["request"]["trip"]

        dest = trip["@destination"]
        fare = float(trip["@fare"])
        origTime = trip["@origTimeMin"]
        destTime = trip["@destTimeMin"]

        data = Data(time, dest, origTime, destTime, fare)

        try:
            client.insertValue(namespaceId, station, data)
            print "Wrote data to " + station
        except Exception as e:
            print "Failed to update for " + station + ": " + str(e)
        del data
    print "Done writing"
    Time.sleep(60)