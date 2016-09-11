class allWifiPoints {
  WifiPoint[] wifiPoints;
  int amountWifi = 0;
  
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
}