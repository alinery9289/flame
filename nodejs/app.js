var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

// -------------------- Redis code -----------------------------------
var redis = require('redis');

var redis_client = redis.createClient(6379, '127.0.0.1');
redis_client.auth(123456)

//connect to redis-server on host:'192.168.6.159'
//var redis_client = redis.createClient(6379, '192.168.6.159');
 
// subscribe function
var sub = function(c) {
    var c = c || 'JOB_FINISH';
    redis_client.subscribe(c, function(e) {
        console.log('starting subscribe channel: ' + c);
    });
};

//Subscribe to the Redis chat channel
redis_client.subscribe('JOB_FINISH');

redis_client.on('error', function(error) {
    console.log(error);
    sub();
});

redis_client.on('message', function(err, msg) {
    console.log('received :' + msg);
    var msgList= msg.split(';',2);
    console.log('msgList[0] :' + msgList[0]);
    console.log('msgList[1] :' + msgList[1]);
    io.emit('chatMessage'+msgList[0], msgList[1]);
});
// -------------------- Redis code finish ------------------------------
