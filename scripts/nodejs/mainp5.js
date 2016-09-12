  var init = false;
function setup() {
  createCanvas(480, 120);

}
function draw() {
  background(255);
//  console.log(init);
  if (init == false) {
    console.log(stationList);
    if (stationList) {
      init = true;
    }
    Object.keys(stationList).forEach(function(key) {
      console.log('init');
      var wifis = stationList[key].split('/'),
        wifiName = wifis[14]
        wifiPower = 100 - +wifis[13] * -1;
        console.log(wifiPower);
        fill(255,0,0,wifiPower);
        ellipse(wifiPower, wifiPower, wifiPower, wifiPower);
      //htmlContent += "<div class='wifiList' style='width:" + wifiPower + "%;'>" + wifiName + "</div>";
    });

  }


}
