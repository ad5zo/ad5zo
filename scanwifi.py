#  scanwifi.py

import os

out = "/tmp/ella"
cmd = "sudo iwlist wlan0 scan > " + out


os.system( cmd )
# cmd = "cat " + out
# os.system( cmd )

f = open( out , "r")
# print(f.read())
# print(f.readline())
# Quality=70/70  Signal level=-39 dBm  


# ESSID:"2WIRE061"

for x in f:
    if x.find( "ESSID" ) > 0:
        print(x.strip())
    if x.find( "Quality" ) > 0:
        print(x.strip())

f.close()
cmd = "rm " + out
os.system( cmd )
