class WifiPoint {

  int x, y;    // Coordinate (center of circle)
  int diameter;    // Diameter of circle (unused == 0).
  String mac;
  String[] dataList;
  
  void init(int idiameter, String iMAC, String iList[]) {
   x = int(random(width));
   y = int(random(height));
   diameter = idiameter;
   mac = iMAC;
   dataList = iList;
   //initialized = true;
  }
  
  
  String[] getParams() {
    return this.dataList;
  }
  
  void printParams() {
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
  
  void create() {
    if (diameter > 0) {
      stroke(0);
      fill(255); //<>//
      ellipse( x, y, diameter, diameter );
      redraw();
    }
  }
  
  void update(int _diameter, String _MAC, String _List[]) {
    this.diameter = _diameter;
    this.mac = _MAC;
    this.dataList = _List;
  }
}