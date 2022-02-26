import dotenv from 'dotenv';
import mqtt from 'mqtt';
import { Automation } from './src/automation-datastructure';

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
    console.log('broker connected');
});

client.on('message', (topic: string, message: Buffer) => {
    const automation: Automation = JSON.parse(message.toString());
    console.log(automation);
});
