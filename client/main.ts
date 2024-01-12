import dotenv from 'dotenv';
import StatusClientBroker from './src/status-client-broker';
import { BrokerInfo } from './src/broker-info';
import CommandClientBroker from './src/command-client-broker';

dotenv.config();

const statusBrokerInfo: BrokerInfo = {
    clientId: `${process.env.CLIENT_ID}`,
    hostname: `ws://${process.env.BROKER_HOST}`,
    port: +process.env.BROKER_PORT,
    timeout: +process.env.PUBLISH_TIMEOUT * 1000,
    topic: process.env.STATUS_TOPIC,
};

const statusClient = new StatusClientBroker(statusBrokerInfo);
statusClient.createClient();

setTimeout(() => {
}, 3000);
