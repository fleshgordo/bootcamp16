# Test your OSC listener

## installation

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

If you are receiving following error, make sure your IP address is correct
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
