## Parse airodump-ng scan data through an OSC relay

You'll need an aircrack installation and a compatible WIFI adapter. Installation instructions: http://www.aircrack-ng.org/

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

# Aircrack part

Put the card into monitor mode
~~~~
airmon-ng start wlan0
~~~~

Start scanning
~~~~
airodump-ng -w dump mon0
~~~~

This should create a dumpXX.csv file in the same folder which is being used by the python script.

# OSC relay
~~~~
python parseCSV2osc.py
~~~~

The skeleton of an OSC message looks like this for accesspoints:

| OSC header    | Type          | # IV packets | ESSID               | Last time seen      | Privacy          | Speed    | LAN IP  | ID Length    |
| ------------- |:-------------:| ------------:| -------------------:| -------------------:| ----------------:| --------:| -------:| ------------:|
| /wifi         | Station       | # number     | 00:00:00:00:00:00   | YYYY-MM-DD HH:MM:SS | OPN, WEP, WPA2   | # number | 0.0.0.0 | # number     |

| Cipher                                    | Auth                   | First time seen     | None | Power                             | ESSID     | Channel | # beacons |
|------------------------------------------:| ----------------------:| -------------------:| ----:| ---------------------------------:| ---------:| -------:| ---------:|
| CCMP, WRAP, TKIP, WEP, WEP40, or WEP104   | MGT, SKA, PSK or OPN   | YYYY-MM-DD HH:MM:SS | None | Signal level reported by the card | WIFI name | # 1-14  | # number  |

The skeleton of an OSC message looks like this for clients:

| OSC header    | Type          | Station MAC        | Last time seen      | Probed ESSID       | First time seen     | Packets  | Power    |
| ------------- |:-------------:| ------------------:| -------------------:| ------------------:| -------------------:| --------:| --------:|
| /wifi         | Client        | 00:00:00:00:00:00  | YYYY-MM-DD HH:MM:SS | 00:00:00:00:00:00  | YYYY-MM-DD HH:MM:SS | # number | # number |
