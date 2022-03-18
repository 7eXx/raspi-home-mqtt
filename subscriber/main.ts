import dotenv from 'dotenv';
import StatusClientBroker from './src/status-client-broker';
import { BrokerInfo } from './src/broker-info';
import CommandClientBroker from './src/command-client-broker';

dotenv.config();

const statusBrokerInfo: BrokerInfo = {
    hostname: `mqtt://${process.env.BROKER_IP}`,
    port: +process.env.BROKER_PORT,
    timeout: +process.env.PUBLISH_TIMEOUT,
    topic: process.env.STATUS_TOPIC,
};

const commandBrokerInfo: BrokerInfo = {
    hostname: `mqtt://${process.env.BROKER_IP}`,
    port: +process.env.BROKER_PORT,
    timeout: +process.env.PUBLISH_TIMEOUT,
    topic: process.env.COMMAND_TOPIC,
};

const statusClient = new StatusClientBroker(statusBrokerInfo);
statusClient.createClient();

const commandClient = new CommandClientBroker(commandBrokerInfo);
commandClient.createClient();

setTimeout(() => {
    commandClient.sendCommand({
        command: 'alarm',
        value: 1,
    });
}, 1000);

setTimeout(() => {
    commandClient.sendCommand({
        command: 'gate',
        value: 1,
    });
}, 3000);
