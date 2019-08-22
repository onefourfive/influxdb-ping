"""
script to test internet connectivity and log it
to influxdb
"""

from influxdb import InfluxDBClient
from pythonping import ping

# iDB_props = {
#     "database": "mydb",
#     "port": "1157",
#     "host": "192.168.1.2"
# }

pingDest = "google.com" #ping doesn't like http://
pingResult = ""

client = InfluxDBClient(database="mydb",
                        port=1157,
                        host="192.168.1.2")

while
response = ping(pingDest, count=1)

if response._responses[0].success:
    pingResult = True
else:
    pingResult = False

datum = [
    {
        "measurement": "connectivity",
        "tags": {
            "site": pingDest,
        },
        "fields": {
            "value": str(pingResult)
        }
    }
]

client.write_points(datum)


