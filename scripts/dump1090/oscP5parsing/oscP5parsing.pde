/**
 * oscP5parsing by hand
 * Fresco Gamba 4.9.2016
 * modified from oscP5 website at http://www.sojamo.de/oscP5
 */

import oscP5.*;
import netP5.*;

OscP5 oscP5;
StringDict allPlanes;
//allPlanes = new StringDict();

void setup() {
  size(400,400);
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 6666 */
  oscP5 = new OscP5(this,7777);
}

void draw() {
  background(0);
}

void oscEvent(OscMessage theOscMessage) {
  /* check if theOscMessage has the address pattern we are looking for. */
  if(theOscMessage.checkAddrPattern("/planes")==true) {
 //println(" typetag: "+theOscMessage.typetag());
    /* check if the typetag is the right one. */
    if(theOscMessage.checkTypetag("sffi")) {
      /* parse theOscMessage and extract the values from the osc message arguments. */
      float lon = theOscMessage.get(2).floatValue();
      String flightnumber = theOscMessage.get(0).stringValue();
      float lat = theOscMessage.get(1).floatValue();
      int altitude = theOscMessage.get(3).intValue();
      print("### received an osc message /planes with typetag ssff.");
      //println(" values: "+flight+", "+squawk+", "+lat+", "+lon);
      println(" values: "+flightnumber+", "+lat+", "+lon + " altitude: "  + altitude);
      return;
    }
  }
}