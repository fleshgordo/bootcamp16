/**
 * oscP5parsing by hand
 * Fresco Gamba 4.9.2016
 * modified from oscP5 website at http://www.sojamo.de/oscP5
 */

import oscP5.*;
import netP5.*;

OscP5 oscP5;

void setup() {
  size(400,400);
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this,6666);
}

void draw() {
  background(0);  
}

void oscEvent(OscMessage theOscMessage) {
  /* check if theOscMessage has the address pattern we are looking for. */
  if(theOscMessage.checkAddrPattern("/planes")==true) {
    println(theOscMessage.typetag());
  
    /* check if the typetag is the right one. */
    if(theOscMessage.checkTypetag("ssff")) {
      /* parse theOscMessage and extract the values from the osc message arguments. */
      float lat = theOscMessage.get(2).floatValue();  
      float lon = theOscMessage.get(3).floatValue();
      String flight = theOscMessage.get(0).stringValue();
      String squawk = theOscMessage.get(1).stringValue();
      print("### received an osc message /planes with typetag ssff.");
      println(" values: "+flight+", "+squawk+", "+lat+", "+lon);
      return;
    }  
  } 
}