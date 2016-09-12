/**
 * oscP5parsing from airodump-ng
 * Fresco Gamba 4.9.2016
 * bootcamp 16
 */

import oscP5.*;
import netP5.*;

OscP5 oscP5;

PFont f;

WifiPoint[]  WifiPoints;
allWifiPoints WifiAll;

int countWifis = 0;
int textOffset = 40;
int marginLeft = 130;
int x = 0;

void setup() {
  size(800,600);
  background(220);
  frameRate(50);
  smooth();
  /* start oscP5, listening for incoming messages at port 6666 */
  oscP5 = new OscP5(this,6666);

  // Create the font
  //printArray(PFont.list());
  f = createFont("Droid Sans", 24);

  WifiPoints = new WifiPoint[50];
  WifiAll = new allWifiPoints();
  WifiAll.init(WifiPoints);
}

void draw() {
  try {
    for (int k=0;k<10;k++) {
      float yPos = textOffset + 30 * k;  
      WifiPoints[k].drawLine(x, yPos);
    }
    x = frameCount % (width - marginLeft);
    if (x == 0) background(220);
  }
  catch (NullPointerException e) {
    //e.printStackTrace();
    println("waiting for osc to become ready - keep calm and move on ... ");
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
        countWifis += 1;
      } //<>//
      return;
    }
  }

}