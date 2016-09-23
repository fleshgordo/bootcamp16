/**
 * oscP5parsing for airodump-ng
 */

import oscP5.*;
import netP5.*;

OscP5 oscP5;

void setup() {
  size(400, 400);
  frameRate(25);

  oscP5 = new OscP5(this, 6666);
}

void draw() {
  background(0);
}

void oscEvent(OscMessage theOscMessage) {
  /* check if theOscMessage has the address pattern we are looking for. */
  if (theOscMessage.checkAddrPattern("/wifi")==true) {
    //println(theOscMessage.arguments());
    //println(theOscMessage.typetag());
    /* check if the typetag is the right one. */
    // stations
    if ( theOscMessage.typetag().equals("sssssssssssss") ) {
      String essid = theOscMessage.get(1).stringValue();
      String power = theOscMessage.get(2).stringValue();
      String bssid = theOscMessage.get(3).stringValue();
      String firstTimeSeen = theOscMessage.get(4).stringValue();
      String lastTimeSeen = theOscMessage.get(8).stringValue();
      String encryption = theOscMessage.get(5).stringValue();
      String packages = theOscMessage.get(10).stringValue();
      String channel = theOscMessage.get(11).stringValue();
      String speed =theOscMessage.get(12).stringValue();
    }
    // clients
     else if ( theOscMessage.typetag().equals("ssssssss") ) {
	String lastTimeSeen = theOscMessage.get(4).stringValue();
      String firstTimeSeen = theOscMessage.get(2).stringValue();
      String stationMAC = theOscMessage.get(5).stringValue();
      String clientMAC = theOscMessage.get(1).stringValue();
      String essid = theOscMessage.get(3).stringValue(); //@MAC duessidnt
      String power = theOscMessage.get(7).stringValue();
    }
  }
}
