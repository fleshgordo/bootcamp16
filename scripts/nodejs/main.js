var stationList = {};
var clientList = {};

var socket = io('http://127.0.0.1:8888');
socket.on('oscMsg', function (data) {
  var wifis = data['args'][0].split('/');
  var wifiType = wifis[1];
  var wifiMAC = wifis[3];

  if (wifiType == "station") {
    // use the MAC addres as unique key for the stationList Object
    // check if key exists, if not add data
    //typeof(stationList[wifiMAC]) != "undefined" ? function() {} : stationList[wifiMAC] = data['args'][0];
    stationList[wifiMAC] = data['args'][0]
  }
  else if (wifiType == "client") {
    clientList[wifiMAC] = data['args'][0]
  }
});

var refreshInterval = setInterval(function()  {
  var htmlContent = ""
  // Object.keys(stationList).forEach(function(key) {
  //   var wifis = stationList[key].split('/'),
  //     wifiName = wifis[14]
  //     wifiPower = 100 - +wifis[13] * -1;
  //   htmlContent += "<div class='wifiList' style='width:" + wifiPower + "%;'>" + wifiName + "</div>";
  // });
  Object.keys(clientList).forEach(function(key) {
    //console.log(clientList[key]);
  });
  document.getElementById("container").innerHTML = htmlContent;
}, 1000);
