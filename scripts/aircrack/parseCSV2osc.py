import subprocess, glob, time, csv, random, argparse
import OSC

# airodump-ng is running and logging the results into a csv file
# with the following command: sudo airodump-ng -o csv -w manuf mon0
# subprocess looks for the last edited csv file in current folder
# this file is parsed by the csv module to find the number of data packets that have passed through the network since the last check

csvs=subprocess.Popen("ls -t1 *csv | head -1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
csv_last=csvs.communicate()[0].strip()

key_value=(' # IV') # look up this value in the scan dump

def lookup(dump):
    datas=[]
    results=[]
    scan=open(dump, "rU")
    next(scan)
    scanDict=csv.DictReader((line.replace('\0','') for line in scan), delimiter=',')
    #return scanDict
    print scanDict
    for aDict in scanDict:
        unwanted = ['', None, False]
        unwantedValues = ['Station MAC','Last time seen','BSSID','Probed ESSIDs','First time seen','# packets','Power']
        aDictClean = {k.strip():v.strip() for k, v in aDict.iteritems() if v not in unwanted}
        #print aDictClean
        msg = ""
        for k, v in aDictClean.items():
            if v not in unwantedValues:
                if k == "LAN IP":
                    v = v.replace(" ", "")
                if k == "Privacy":
                    if v == "WPA" or v == "WEP" or v == "WPA2" or v == "OPN" or v == "WPA2WPA":
                        msg = "/station%s" %msg
                    else:
                        msg = "/client%s" %msg
                if v == "":
                    v = "None"
                msg += "/%s" %v
        if msg != "":
            print "sending osc: %s" %msg
            OSCmsg=OSC.OSCMessage()
            OSCmsg.setAddress('/wifi')
            OSCmsg.append(msg)
            c.send(OSCmsg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    default_ip = "0.0.0.0"
    default_port = 5005
    parser.add_argument("--ip", default=default_ip,
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=default_port,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    ### OSC
    send_address = args.ip, args.port
    c = OSC.OSCClient()
    c.connect( send_address )

    new_packet_list=lookup(csv_last)
