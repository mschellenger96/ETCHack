import requests
import json

base = "http://api.bart.gov/api/sched.aspx?cmd=depart&orig=SANL&dest={0}&date=now&key=MW9S-E7SL-26DU-VV8V&b=0&a=1&l=1&json=y"
stations = ["12th", "16th", "19th", "24th", "ashb", "antc", "balb", 
"bayf", "cast", "civc", "cols", "colm", "conc", "daly", "dbrk", "dubl", 
"deln", "plza", "embr", "frmt", "ftvl", "glen", "hayw", "lafy", "lake", 
"mcar", "mlbr", "mont", "nbrk", "ncon", "oakl", "orin", "pitt", "pctr", 
"phil", "powl", "rich", "rock", "sbrn", "sfia", "shay", "ssan", "ucty", 
"warm", "wcrk", "wdub", "woak"]

for station in stations:
    r = requests.get(base.format(station))
    j = r.json()
    trip = j["root"]["schedule"]["request"]["trip"]
    dest = trip["@destination"]
    fare = float(trip["@fare"])
    origTime = trip["@origTimeMin"]
    destTime = trip["@destTimeMin"]

    print dest
    print fare
    print origTime
    print destTime
    print