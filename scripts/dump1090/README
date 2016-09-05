## dump1090 -> parsing dump1090 data through an OSC relay

# Installation according to:
https://github.com/antirez/dump1090

# start with net and interactive mode
~~~~
./dump1090 --interactive --net
~~~~

this should produce a data.json available at
~~~~
http://localhost:8080/data.json
~~~~

check if this works!

# OSC relay
Now we can start our python JSON - OSC relay with

~~~~
python dump1090json2osc.py
~~~~

This script works in OSC multiclient mode - hence multiple client addresses can be defined.
Look at the targets dictionary.

# Receive data

Test the OSC server
~~~~
python OSCserverLocalhost.py
~~~~

Check out the processing sketch called oscP5parsing.pde for capturing data in processing.
You'll need the oscP5 library
