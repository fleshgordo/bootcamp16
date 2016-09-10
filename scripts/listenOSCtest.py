import OSC, argparse

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

if __name__ == "__main__":
    print """Usage: specify IP address of OSC sender with --ip parameter and portnumber with --port
    example: python OSCserver.py --ip 192.168.10.1 --port 7777
    default values are 127.0.0.1 and port 6666
    """
    parser = argparse.ArgumentParser()
    default_ip = "127.0.0.1"
    default_port = 6666
    parser.add_argument("--ip", default=default_ip,
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=default_port,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    receive_address = args.ip, args.port

    print "listening for OSC messages on ip: %s and port: %s" %(args.ip, args.port)
    s = OSC.OSCServer(receive_address)  # listen on localhost, port 57120
    # this is put into a config file for easy mod'ing
    OSCPATH = ['/gsm','/wifi','/planes']
    for path in OSCPATH:
        s.addMsgHandler(path, handler)     # call handler() for OSC messages received with the /startup address
    s.serve_forever()
