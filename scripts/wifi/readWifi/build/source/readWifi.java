import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import oscP5.*; 
import netP5.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class readWifi extends PApplet {

/**
 * oscP5parsing by hand
 * Fresco Gamba 4.9.2016
 * modified from oscP5 website at http://www.sojamo.de/oscP5
 */




OscP5 oscP5;

PFont f;

WifiPoint[]  WifiPoints;
int countWifis = 0;
float y = 100;
public void setup() {
  
  background(255);
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 6666 */
  oscP5 = new OscP5(this,6666);

  // Create the font
  //printArray(PFont.list());
  f = createFont("Helvetica", 24);

  WifiPoints = new WifiPoint[50];
y = height * 0.5f;
noLoop();
}

public void draw() {
  line(0, y, width, y);

  y = y - 1;
  if (y < 0) {
    y = height;
  }
}

public void oscEvent(OscMessage theOscMessage) {

  /* check if theOscMessage has the address pattern we are looking for. */
  if(theOscMessage.checkAddrPattern("/wifi")==true) {
    /* check if the typetag is the right one. */
    if(theOscMessage.checkTypetag("s")) {
      /* parse theOscMessage and extract the values from the osc message arguments. */
      String[] list = split(theOscMessage.get(0).stringValue(), '/');
      String WifiType = list[1];
      //println(WifiType);
      if (WifiType.equals("client")) {

      }
      else if (WifiType.equals("station")) {
        WifiPoints[countWifis] = new WifiPoint();

        int diameter = PApplet.parseInt(PApplet.parseInt(list[13]) * -1);
        String mac = list[3];
        WifiPoints[countWifis].init(diameter, mac, list);
        WifiPoints[countWifis].show();
        //WifiPoints[countWifis].printParams();
        countWifis += 1;
      }
      else if (WifiType.equals("EOF")) {
        countWifis = 0;
        loop();
        //background(0);   // Set the background to black

      }
      return;
    }
  }

}

public void mousePressed() {
  line(mouseX, 10, mouseX, 90);
}
class WifiPoint {

  int x, y;    // Coordinate (center of circle)
  int diameter;    // Diameter of circle (unused == 0).
  String mac;
  String[] dataList;

  public void init(int idiameter, String iMAC, String iList[]) {
   x = PApplet.parseInt(random(width));
   y = PApplet.parseInt(random(height));
   diameter = idiameter;
   mac = iMAC;
   dataList = iList;
  }

  public void printParams() {
    print("This wifiPoint has MAC address: ");
    print(this.mac);
    print(", x: ");
    print(this.x);
    print(", y: ");
    print(this.y);
    print(", diameter: ");
    print(this.diameter);
    print(", list: ");
    println(this.dataList);
  }
  public void show() {
    if (diameter > 0) {
      stroke(0);
      fill(255);
      ellipse( x, y, diameter, diameter );
      //fill(128);
      print("drawing ellipse with coordinates: ");
      print(this.x);
      print(this.y);
      print(" diameter");
      print(this.diameter);
      println ("");
      redraw();
    }
  }

}
  public void settings() {  size(800,600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "readWifi" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
