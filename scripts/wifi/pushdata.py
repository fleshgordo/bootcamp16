#!/usr/local/bin/python3
# coding=utf8
import subprocess, csv
from io import StringIO
import io
import subprocess, glob, time, csv, random, argparse
import pprint
from pythonosc import osc_message_builder
from pythonosc import udp_client

# pretty print is neat
pp = pprint.PrettyPrinter(indent=2)

def sortList(_list, _key):
    return sorted(_list, key=lambda x: x[_key])

def buildOscMessage(_dest, _dict):
    for entry in range(len(_dict)):
        Oscmsg = osc_message_builder.OscMessageBuilder(address="/wifi")
        Oscmsg.add_arg(_dest)
        for k, v in _dict[entry].items():
            if (v == "" or v == None):
                v = "None"
            Oscmsg.add_arg(str(v.strip()))
        SendOSC = Oscmsg.build()
        c.send(SendOSC)
        #print ("sending osc")

def lookup():
    # get the newest capture.csv file, then use awk to get only Station data
    stations = r"cat `ls -t1 *csv | tail -n 1` |  awk '/BSSID,/{y=1;next}y' | gsed -e 's/\r//g' -e '/^$/q'"
    #dataStation = subprocess.Popen(stations, stdin=None, stdout=subprocess.PIPE, stderr=None, shell=True)
    dataStation = subprocess.Popen(stations, shell=True, stdout=subprocess.PIPE).stdout.read()
    fS = io.StringIO(str(dataStation.decode('utf-8')))

    #print (str(dataStation))
    # get the newest capture.csv file, then use awk to get only Station data
    clients = r"cat `ls -t1 *csv | tail -n 1` | awk '/Station/{y=1;next}y'"
    #dataClients = subprocess.Popen(clients, shell=True, stdout=subprocess.PIPE).stdout.read()
    dataClients = subprocess.Popen(clients, stdout=subprocess.PIPE, shell=True).stdout.read()
    # str(dataClients.decode('utf-8')
    f = io.StringIO(str(dataClients.decode('utf-8')))

    # convert the data to a list of dict() objects
    convClient = lambda row: {'station_mac':row[0].strip(), 'first_time_seen':row[1].strip(), 'last_time_seen':row[2].strip(), 'power':row[3].strip(), 'packets':row[4].strip(), 'bssid':row[5].strip(), 'probed essid': row[6].strip()}

    # convert the data to a list of dict() objects
    convStation = lambda row: {'station_mac':row[0].strip(), 'first_time_seen':row[1].strip(), 'last_time_seen':row[2].strip(), 'channel': row[3].strip(), 'speed':row[4].strip(), 'privacy': row[5].strip(), 'cipher': row[6].strip(), 'auth': row[7].strip(), 'power': row[8].strip(), 'beacons': row[9].strip(), 'packets': row[10].strip(), 'essid': row[13].strip()}

    dataClient = [row for row in csv.reader(f, delimiter=',') if len(row) != 0]
    dictClient = [convClient(row) for row in dataClient]


    dataStation = [row for row in csv.reader(fS, delimiter=',') if len(row) != 0]
    dictStation = [convStation(row) for row in dataStation]

    # SORTING ------
    # sort by power
    dictClient = sorted(dictClient, key=lambda x: x["power"])

    # sort by power
    dictStation = sorted(dictStation, key=lambda x: x["power"])

    pp.pprint(dictStation)
    pp.pprint(dictClient)

    buildOscMessage("client",dictClient)
    buildOscMessage("station",dictStation)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    default_ip = "127.0.0.1"
    default_port = 6666
    parser.add_argument("--ip", default=default_ip,
    help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=default_port,
    help="The port the OSC server is listening on")
    args = parser.parse_args()

    c = udp_client.UDPClient(args.ip, args.port)
    ### Endless loop
    while True:
        lookup()
        time.sleep(1)
