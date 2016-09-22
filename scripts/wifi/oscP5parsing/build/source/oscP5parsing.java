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
 * oscP5parsing by andreas schlegel
 * example shows how to parse incoming osc messages "by hand".
 * it is recommended to take a look at oscP5plug for an
 * alternative and more convenient way to parse messages.
 * oscP5 website at http://www.sojamo.de/oscP5
 */




OscP5 oscP5;
NetAddress myRemoteLocation;

public void setup() {
  
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this, 6666);

  /* myRemoteLocation is a NetAddress. a NetAddress takes 2 parameters,
   * an ip address and a port number. myRemoteLocation is used as parameter in
   * oscP5.send() when sending osc packets to another computer, device,
   * application. usage see below. for testing purposes the listening port
   * and the port of the remote location address are the same, hence you will
   * send messages back to this sketch.
   */
  //myRemoteLocation = new NetAddress("127.0.0.1",12000);
}

public void draw() {
  background(0);
}

public void oscEvent(OscMessage theOscMessage) {
  /* check if theOscMessage has the address pattern we are looking for. */

  if (theOscMessage.checkAddrPattern("/wifi")==true) {
    /* check if the typetag is the right one. */
    //println(theOscMessage.arguments());
    //println(theOscMessage.typetag());
    // stations
    if ( theOscMessage.typetag().equals("sssssssssssss") ) {
      //println(theOscMessage.arguments());
      String essid = theOscMessage.get(1).stringValue();
      String power = theOscMessage.get(2).stringValue();
      String bssid = theOscMessage.get(3).stringValue();
      String firstTimeSeen = theOscMessage.get(4).stringValue();
      String lastTimeSeen = theOscMessage.get(8).stringValue();
      String encryption = theOscMessage.get(5).stringValue();
      String packages = theOscMessage.get(10).stringValue();
      String channel = theOscMessage.get(11).stringValue();
      String speed =theOscMessage.get(12).stringValue();
      //println (packages, speed);
      //String
      //println (ESSID);
    }
    // clients
     else if ( theOscMessage.typetag().equals("ssssssss") ) {
       String lastTimeSeen = theOscMessage.get(7).stringValue();
       String firstTimeSeen = theOscMessage.get(2).stringValue();
       String probes = theOscMessage.get(1).stringValue();
       String essid = theOscMessage.get(3).stringValue();
       String power = theOscMessage.get(4).stringValue();
       println(probes, power);
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
