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

public class oscP5parsing extends PApplet {

/**
 * oscP5parsing for airodump-ng
 */




OscP5 oscP5;

public void setup() {
  
  frameRate(25);
  
  oscP5 = new OscP5(this, 6666);
}

public void draw() {
  background(0);
}

public void oscEvent(OscMessage theOscMessage) {
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
       String lastTimeSeen = theOscMessage.get(7).stringValue();
       String firstTimeSeen = theOscMessage.get(2).stringValue();
       String probes = theOscMessage.get(1).stringValue();
       String essid = theOscMessage.get(3).stringValue();
       String power = theOscMessage.get(4).stringValue();
       println(theOscMessage.arguments());
    }
  }
}
  public void settings() {  size(400, 400); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "oscP5parsing" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
