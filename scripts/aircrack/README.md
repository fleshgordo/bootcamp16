## Parse airodump-ng scan data through an OSC relay

You'll need an aircrack installation and a compatible WIFI adapter. Installation instructions: http://www.aircrack-ng.org/

Put the card into monitor mode
~~~~
airmon-ng start wlan0
~~~~

Start scanning
~~~~
airodump-ng -w dump mon0
~~~~

This should create a dumpXX.csv file in the same folder which is being used by the python script.

~~~~
python parseCSV2osc.py
~~~~

The skeleton of an OSC message looks like this for accesspoints:

| OSC header    | Type          | BSSID              |
| ------------- |:-------------:| ------------------:|
| /wifi         | /station      | /00:00:00:00:00:00 |
