import mqtt, { MqttClient } from 'mqtt';
import { BrokerInfo } from './broker-info';
import { Command } from './command';

export default class CommandClientBroker {
    private client: MqttClient;

    constructor(private brokerInfo: BrokerInfo) {
    }

    public createClient(): void {
        this.client = mqtt.connect(this.brokerInfo.hostname, {
            port: this.brokerInfo.port,
            connectTimeout: this.brokerInfo.timeout,
        });

        this.client.on('connect', () => {
            console.log('command broker connected');
        });
    }

    public sendCommand(command: Command) {
        if (!this.client.connected) {
            return;
        }

        this.client.publish(this.brokerInfo.topic, JSON.stringify(command));
    }
}
