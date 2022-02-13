import dotenv from 'dotenv';
import mqtt from 'mqtt';
import { SystemInformation } from './src/system-information';

dotenv.config();

const brokerInfo = {
    hostname: `mqtt://${process.env.BROKER_IP}`,
    port: +process.env.BROKER_PORT,
    timeout: process.env.PUBLISH_TIMEOUT,
    topic: process.env.TOPIC,
};

console.log(brokerInfo);

const client = mqtt.connect(brokerInfo.hostname, { port: brokerInfo.port });

client.on('connect', () => {
    client.subscribe(brokerInfo.topic);
});

client.on('message', (topic: string, message: Buffer) => {
    const systemInformation: SystemInformation = JSON.parse(message.toString());
    console.log(systemInformation);
});
