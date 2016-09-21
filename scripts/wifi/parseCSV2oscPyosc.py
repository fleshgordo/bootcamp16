#!/usr/local/bin/python3
# coding=utf8

import subprocess, glob, time, csv, random, argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client


# airodump-ng is running and logging the results into a csv file
# with the following command: sudo airodump-ng -o csv -w manuf mon0
# subprocess looks for the last edited csv file in current folder
# this file is parsed by the csv module to find the number of data packets that have passed through the network since the last check

csvs=subprocess.Popen("ls -t1 *csv | head -1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
csv_last=csvs.communicate()[0].strip()

def lookup(dump):
    datas=[]
    results=[]
    scan=open(dump, "rU",encoding='utf-8', errors='ignore')
    next(scan)
    scanDict=csv.DictReader((line.replace('\0','') for line in scan), delimiter=',' )
    for aDict in scanDict:
        Oscmsg = osc_message_builder.OscMessageBuilder(address="/wifi")
        unwanted = ['', None, False]
        print(aDict)
        aDictClean = {k.strip():v.strip() for k, v in aDict.items() if v not in unwanted}
        msg = ""
        for k, v in aDictClean.items():
            #if v not in unwanted:
            if k == "LAN IP":
                v = v.replace(" ", "")
			# seperate between clients and stations
            if k == "Privacy":
                if v == "WPA" or v == "WEP" or v == "WPA2" or v == "OPN" or v == "WPA2WPA":
                    Oscmsg.add_arg("station")
                else:
                    Oscmsg.add_arg("client")
            if v == "":
                v = "None"
            Oscmsg.add_arg(v)
        SendOSC = Oscmsg.build()
        c.send(SendOSC)
        print(Oscmsg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    default_ip = "192.168.10.104"
    default_port = 6666
    parser.add_argument("--ip", default=default_ip,
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=default_port,
    help="The port the OSC server is listening on")
    args = parser.parse_args()

    c = udp_client.UDPClient(args.ip, args.port)
    ### Endless loop
    while True:
        lookup(csv_last)
        msg = osc_message_builder.OscMessageBuilder(address="/wifi")
        msg.add_arg("/EOF")
        msg = msg.build()
        c.send(msg)
        print(msg)
        time.sleep(1)
