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
  /* start oscP5, listening for incoming messages at port 6666 */
  oscP5 = new OscP5(this,6666);
}

void draw() {
  background(0);  
}

void oscEvent(OscMessage theOscMessage) {
  /* check if theOscMessage has the address pattern we are looking for. */
  if(theOscMessage.checkAddrPattern("/wifi")==true) {
    /* check if the typetag is the right one. */
    if(theOscMessage.checkTypetag("s")) {
      /* parse theOscMessage and extract the values from the osc message arguments. */
      String[] list = split(theOscMessage.get(0).stringValue(), '/');
      String WifiType = list[1];
      //println(WifiType);
      if (WifiType.equals("client")) {
        print("##### clients #### ");
        //println(list[2]); 
      }
      else if (WifiType.equals("station")) {
        print("##### station #### ");
        println(list[14]); 
      }
      return;
    }  
  } 
}