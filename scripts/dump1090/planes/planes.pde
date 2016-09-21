import netP5.*;
import oscP5.*;

OscP5 oscP5;
String flightnumber = "";
float lat, lon;
int altitude;

void setup() {
  size(400, 400);
  oscP5 = new OscP5(this, 7777);
  background(255);
}

void draw() {
  //println("there'll be dragons no planes");
  //background(0);
  
  
  float latScreen = map(lat, 45, 47, 0, width);
  float lonScreen = map(lon, 6 , 7, 0, height);
  println(lat,lon);
  println(latScreen, lonScreen);
  //text(flightnumber, latScreen, lonScreen);
  stroke(1);
  strokeWeight(2);
  point(latScreen,lonScreen);
}

void oscEvent(OscMessage theOscMessage) {
  //println(theOscMessage.arguments());
  //println(theOscMessage.typetag());
  flightnumber = theOscMessage.get(0).stringValue();
  lat = theOscMessage.get(1).floatValue();
  lon = theOscMessage.get(2).floatValue();
  altitude = theOscMessage.get(3).intValue();
}