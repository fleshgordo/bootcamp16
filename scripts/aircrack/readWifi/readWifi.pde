/**
 * oscP5parsing by hand
 * Fresco Gamba 4.9.2016
 * modified from oscP5 website at http://www.sojamo.de/oscP5
 */

import oscP5.*;
import netP5.*;

OscP5 oscP5;

PFont f;

void setup() {
  size(400,400);
  frameRate(25);
  /* start oscP5, listening for incoming messages at port 6666 */
  oscP5 = new OscP5(this,6666);

  // Create the font
  //printArray(PFont.list());
  f = createFont("Helvetica", 24);
  textFont(f);
  background(102);
  textAlign(RIGHT);
  drawType("test",width * 0.25);
  noLoop();
}

void draw() {
   redraw();
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
        //print("##### clients #### ");
        //println(list[2]); 
      }
      else if (WifiType.equals("station")) {
        print("##### station #### ");
        print ("power: ");
        print(list[14]); 
        
        int Power = int(list[13]);
        println(Power);
        textAlign(CENTER);
        drawType(list[14], Power * -5);
      }
      return;
    }  
  } 

}
void drawType(String content, float x) {
  //print(content);
          print("drawing text at pos: ");
          println(x);
          stroke(255);
  line(x, 0, x, 65);
  line(x, 220, x, height);
  fill(128);translate(width/2, height/2);
rotate(PI/3.0);
  text(content, x, 95);
  fill(51);
  redraw();

}
void mousePressed() {
  line(mouseX, 10, mouseX, 90);
}