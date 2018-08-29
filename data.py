import json

class Data:

    def __init__(self, time, destination, leaveTime, arriveTime, fare):
        self.time = time
        self.destination = destination
        self.leaveTime = leaveTime
        self.arriveTime = arriveTime
        self.fare = fare

    def __init__(self):
        self.time = None
        self.destination = None
        self.leaveTime = None
        self.arriveTime = None
        self.fare = None

    @property
    def Time(self):
        return self.time
    @Time.setter
    def Time(self, time):
        self.time = time

    @property
    def Destination(self):
        return self.destination
    @Destination.setter
    def Destination(self, destination):
        self.destination = destination

    @property
    def LeaveTime(self):
        return self.leaveTime
    @LeaveTime.setter
    def LeaveTime(self, leaveTime):
        self.leaveTime = leaveTime

    @property
    def ArriveTime(self):
        return self.arriveTime
    @ArriveTime.setter
    def ArriveTime(self, arriveTime):
        self.arriveTime = arriveTime

    @property
    def Fare(self):
        return self.fare
    @Fare.setter
    def time(self, fare):
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

    @staticmethod
    def fromDictionary(content):
        data = Data()

        if len(content) == 0:
            return data

        properties = inspect.getmembers(Data, lambda o: isinstance(o, property))
        for p in properties:
            print p
            if p[0] in content:
                setattr(data, p[0], content[p[0]])
        return data

    @staticmethod
    def fromJson(jsonObj):
        return Data.fromDictionary(jsonObj)
