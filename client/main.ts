import dotenv from 'dotenv';
import StatusClientBroker from './src/status-client-broker';
import { BrokerInfo } from './src/broker-info';
import CommandClientBroker from './src/command-client-broker';

dotenv.config();

const statusBrokerInfo: BrokerInfo = {
    hostname: `ws://${process.env.BROKER_IP}`,
    port: +process.env.BROKER_PORT,
    timeout: +process.env.PUBLISH_TIMEOUT,
    topic: process.env.STATUS_TOPIC,
};

const statusClient = new StatusClientBroker(statusBrokerInfo);
statusClient.createClient();

setTimeout(() => {
}, 3000);
