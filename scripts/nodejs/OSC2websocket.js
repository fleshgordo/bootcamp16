var app = require('http').createServer(handler)
var io = require('socket.io')(app);
var fs = require('fs');
var osc = require("osc"),
    http = require("http");

// OSC parts

var ipAddress = "192.168.10.235",
 portNumber = 6666;

// websocket parts
app.listen(8888);

function handler (req, res) {
  fs.readFile(__dirname + '/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(200);
    res.end(data);
  });
}

io.on('connection', function (socket) {
  udpPort.on("message", function (oscMsg) {
      console.log("An OSC message just arrived!", oscMsg);
      socket.emit('oscMsg', oscMsg);
  });
});

// osc part

// Create an osc.js UDP Port listening on port 57121.
var udpPort = new osc.UDPPort({
    localAddress: ipAddress,
    localPort: portNumber
});

// Open the socket.
udpPort.open();
