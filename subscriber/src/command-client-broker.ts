import mqtt, { MqttClient } from 'mqtt';
import { BrokerInfo } from './broker-info';

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
            console.log('broker connected');
            const command = '{ "command": "alarm", value: 1 }';
            this.client.publish(this.brokerInfo.topic, command);
        });
    }
}
