from SdsClient import SdsClient
from SdsStream import SdsStream

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

for station in stations:
    stream = SdsStream()
    stream.Id = station
    stream.Name = station + " station"
    stream.Description = "A Stream to store the BART events"
    stream.TypeId = "bartType"

    client.createOrUpdateStream(namespaceId, stream)
    print "Created stream ID " + station