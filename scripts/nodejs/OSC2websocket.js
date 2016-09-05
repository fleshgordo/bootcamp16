var app = require('http').createServer(handler)
var io = require('socket.io')(app);
var fs = require('fs');
var osc = require("osc"),
    http = require("http");

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
    localAddress: "127.0.0.1",
    localPort: 5005
});

// Open the socket.
udpPort.open();
