#!/usr/bin/python
#
# dump1090 JSon file to opensoundcontrol
#
# Uses the Requests library to compare the state of planes in view
# and prints changes to standard out
#
# Json compare script orginally written by
# @th0ma5 on twitter
# http://th0ma5w.github.io
#

import requests, json, datetime, time, random, argparse
import OSC

get_data = lambda : json.loads(requests.get('http://127.0.0.1:8080/data.json').content)
data_diff = lambda new,old : [x for x in new if x not in old]
make_date = lambda : str(datetime.datetime.now())

old_data = []

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

    if (args.ip == default_ip and args.port == default_port):
        c = OSC.OSCMultiClient()
        # Add more cliens for workshop participants
        targets = {
			('224.0.0.1',7777):('/planes',{'':True})
#('192.168.1.118',7777):('/planes',{'':True})
        }
        c.updateOSCTargets(targets)
    else:
        c = OSC.OSCClient()
        c.connect( send_address )

    while True:
            #try:
            new_data = get_data()
            diffs = data_diff(new_data,old_data)
            old_data = new_data
            if len(diffs) > 0:
                diff_lines = [','.join([str(y).strip() for y in [make_date()] + x.values()]) for x in diffs]
                for line in diff_lines:
                    print line
                    msg=OSC.OSCMessage()
                    #msg.setAddress('/planes')
                    msg.append(x['flight'])
                    msg.append(x['squawk'])
                    msg.append(x['lat'])
                    msg.append(x['lon'])
                    c.send(msg)
                    #b.send(msg)
                    print msg

            #except:
            #    pass
            time.sleep(0.5)
