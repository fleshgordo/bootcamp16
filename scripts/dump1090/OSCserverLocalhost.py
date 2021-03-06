import OSC

print("listening on 127.0.0.1 port 7777")
def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

if __name__ == "__main__":
    s = OSC.OSCServer(('127.0.0.1', 7777))  # listen on localhost, port 7777
    s.addMsgHandler('/planes', handler)     # call handler() for OSC messages received with the /startup address
    s.serve_forever()
