/**
 * oscP5parsing by hand
 * Fresco Gamba 4.9.2016
 * modified from oscP5 website at http://www.sojamo.de/oscP5
 */

import oscP5.*;
import netP5.*;

OscP5 oscP5;

PFont f;

WifiPoint[]  WifiPoints;
allWifiPoints WifiAll;

int countWifis = 0;

void setup() {
  size(800,600);
  background(255);
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 6666 */
  oscP5 = new OscP5(this,6666);

  // Create the font
  //printArray(PFont.list());
  f = createFont("Helvetica", 24);

  WifiPoints = new WifiPoint[50];
  WifiAll = new allWifiPoints();
  WifiAll.init(WifiPoints);
}

void draw() {
  try {
    //WifiAll.printAll();
    WifiAll.renderAll();
  }
  catch (NullPointerException e) {
    e.printStackTrace();
  }
}

void oscEvent(OscMessage theOscMessage) {

  /* check if theOscMessage has the address pattern we are looking for. */
  if(theOscMessage.checkAddrPattern("/wifi")==true) {
    /* check if the typetag is the right one. */
    if(theOscMessage.checkTypetag("s")) {
      /* parse theOscMessage and extract the values from the osc message arguments. */
      String[] list = split(theOscMessage.get(0).stringValue(), '/');
      String WifiType = list[1];
      if (WifiType.equals("EOF")) {
        WifiAll.updateAmount(countWifis);
        countWifis = 0;
        return;
      }
      if (WifiType.equals("client")) {

      }
      if (WifiType.equals("station")) {
        int diameter = int(list[13]);
        diameter *= -1;
        String mac = list[3];
        if (WifiPoints[countWifis] == null) {
          WifiPoints[countWifis] = new WifiPoint();
          WifiPoints[countWifis].init(diameter, mac, list);
        }
        else {
          diameter = int(random(120));
          WifiPoints[countWifis].update(diameter, mac, list);
        }
        WifiPoints[countWifis].printParams();
        
        countWifis += 1;
      }
       //<>//
      return;
    }
  }

}