var server = require('express')();

server.use('/hello', require('./routes/hello.js'));
server.use('/v1/messages', require('./routes/messages.js'));

module.exports = server;
