import subprocess, glob, time, csv, random, argparse
import OSC

# airodump-ng is running and logging the results into a csv file
# with the following command: sudo airodump-ng -o csv -w manuf mon0
# subprocess looks for the last edited csv file in current folder
# this file is parsed by the csv module to find the number of data packets that have passed through the network since the last check

# Add more cliens for workshop participants
targets = {
    ('0.0.0.0',6666):('/wifi',{'':True}),
    ('127.0.0.1',6666):('/wifi',{'':True})
}

csvs=subprocess.Popen("ls -t1 *csv | head -1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
csv_last=csvs.communicate()[0].strip()

def lookup(dump):
    datas=[]
    results=[]
    scan=open(dump, "rU")
    next(scan)
    scanDict=csv.DictReader((line.replace('\0','') for line in scan), delimiter=',')
    countStations = 0
    countClients = 0
    for aDict in scanDict:
        try:
    		unwanted = ['', None, False]
    		unwantedValues = ['Station MAC','Last time seen','BSSID','Probed ESSIDs','First time seen','# packets','Power']
    		aDictClean = {k.strip():v.strip() for k, v in aDict.iteritems() if v not in unwanted}
    		msg = ""
    		for k, v in aDictClean.items():
    		    if v not in unwantedValues:
    			if k == "LAN IP":
    			    v = v.replace(" ", "")
    			# seperate between clients and stations
    			if k == "Privacy":
    			    if v == "WPA" or v == "WEP" or v == "WPA2" or v == "OPN" or v == "WPA2WPA":
    				msg = "/station%s" %msg
    				countStations += 1
    			    else:
    				msg = "/client%s" %msg
    				countClients += 1
    			if v == "":
    			    v = "None"
    			# compose OSC message
    			msg += "/%s" %v
    		# only send OSC if message is not empty
    		if msg != "":
    		    OSCmsg=OSC.OSCMessage()
    		    OSCmsg.append(msg)
    		    c.send(OSCmsg)
    		    print OSCmsg
        except:
            pass
    # sending EOF for OSC dump
    OSCmsgEOF=OSC.OSCMessage()
    OSCmsgEOF.append("/EOF")
    c.send(OSCmsgEOF)
    print OSCmsgEOF
    #return countStations, countClients

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    default_ip = "0.0.0.0"
    default_port = 6666
    parser.add_argument("--ip", default=default_ip,
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=default_port,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    ### OSC
    c = OSC.OSCMultiClient()
    c.updateOSCTargets(targets)

    ### Endless loop
    while True:
        lookup(csv_last)
        time.sleep(1)
