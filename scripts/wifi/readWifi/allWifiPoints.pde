class allWifiPoints {
  WifiPoint[] wifiPoints;
  
  int amountWifi = 0;
  float margin = 130;
  float xline, yline;
  float paddingVertical = 50;
  
  void init(WifiPoint[] _WifiPoint) {
    wifiPoints = _WifiPoint;
  }
  void printAll() {
    for (int j=0;j<amountWifi;j++) {
      println(this.wifiPoints[j].mac);
    }
  }
  void update(int index, String _mac, String[] _list) {
    this.wifiPoints[index].dataList = _list;
    this.wifiPoints[index].mac = _mac;
  }
  void updateAmount(int _update) {
    this.amountWifi = _update;
  }
  void renderAll() {
    background(0);
    for(int j=0;j<this.amountWifi;j++) {
      this.wifiPoints[j].create();
    }
  }
  
  void drawLine() {
    for (int k=0;k<10;k++) {
      float yPos = textOffset + paddingVertical * k;  
      
      String wifiName = this.wifiPoints[k].dataList[14];
      float wifiPower =  100 + float(this.wifiPoints[k].dataList[13]);
      float yWifiPos = map(wifiPower, 0, 100, yPos, yPos-10);
      
      fill(0);
      text(wifiName, 10, yPos);
      point(margin + this.xline, yWifiPos);
      //WifiPoints[k].drawLine(x, yPos);
    }
    this.xline = frameCount % (width - margin);
    if (this.xline == 0) background(220);
  }
  
  void createCircles() {
    
//background(255);
    for (int k=0;k<10;k++) {
      float diameter = 100 - ( -1* float(this.wifiPoints[k].dataList[13]));
      float x = random(width);
      float y = random(height);
      //print("drawing circles: ");
      //print(diameter);
      //print(" ");
      //print(x);
      //print(" ");
      //println(y);
      if (diameter > 0) {
        stroke(0);
        fill(255);
        ellipse( x, y, diameter, diameter);
      }
    }
  }
}