import json

class Data:
    def __init__(self, time, destination, leaveTime, arriveTime, fare):
        self.time = time
        self.destination = destination
        self.leaveTime = leaveTime
        self.arriveTime = arriveTime
        self.fare = fare

    def toJson(self):
        myDict = {
            'Destination' : self.destination, 
            'Time' : self.time, 
            'LeaveTime' : self.leaveTime, 
            'ArriveTime' : self.arriveTime, 
            'Fare' : self.fare
        }
        return json.dumps(myDict)