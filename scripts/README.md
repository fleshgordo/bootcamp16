# Test your OSC listener

## Installation

Before starting, make sure you have pyOSC library for python installed:
~~~~
sudo pip install pyOSC
~~~~

(If pip installer for some reason isn't working, download the tarball file directly from: https://pypi.python.org/pypi/pyOSC)
~~~~
tar -xvf pyOSC-0.3.5b-5294.tar.gz
cd pyOSC*
sudo python setup.py install
~~~~

# Usage

Check your current IP address (ifconfig) and make sure you are connected to the same subnet as the OSC sender. You'll need to know the port number as well.
Example:

~~~~
python listenOSCtest.py --ip 192.168.1.55 --port 5005
~~~~

All's working, if you are receiving an output like this:
~~~~
OSCMessage '/wifi' from ('192.168.10.53', 36562): ['/client/00:02:2D:5B:6E:D7/2016-04-15 02:52:47/(not associated)/2016-04-15 02:52:37/5/-48']
~~~~

# Troubleshoot

If you are receiving following error, make sure your IP address is correct:
~~~~
File "listenOSCtest.py", line 25, in <module>
   s = OSC.OSCServer(receive_address)  # listen on localhost, port 57120
 File "/Users/fresco/anaconda2/lib/python2.7/site-packages/OSC.py", line 1765, in __init__
   UDPServer.__init__(self, server_address, self.RequestHandlerClass)
 File "/Users/fresco/anaconda2/lib/python2.7/SocketServer.py", line 420, in __init__
   self.server_bind()
 File "/Users/fresco/anaconda2/lib/python2.7/SocketServer.py", line 434, in server_bind
   self.socket.bind(self.server_address)
 File "/Users/fresco/anaconda2/lib/python2.7/socket.py", line 228, in meth
   return getattr(self._sock,name)(*args)
socket.error: [Errno 49] Can't assign requested address
~~~~

If you can't see any output in the terminal (like below), make sure the OSC sender part is using your IP address as target:
~~~~
listening for OSC messages on ip: 192.168.xxx.xxx and port: xxxx
~~~~

If your IP is correct and it has been specified on the sender side, make sure your OSC header address is mentioned in the list (listenOSCtest.py):
~~~~
OSCPATH = ['/gsm','/wifi','/planes']
~~~~
