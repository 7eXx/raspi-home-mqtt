import mqtt, { MqttClient } from 'mqtt';
import { Automation } from './automation-datastructure';
import { BrokerInfo } from './broker-info';

export default class StatusClientBroker {
    private client: MqttClient;

    constructor(private brokerInfo: BrokerInfo) {
    }

    public createClient(): void {
        this.client = mqtt.connect(this.brokerInfo.hostname, {
            port: this.brokerInfo.port,
            connectTimeout: this.brokerInfo.timeout,
        });

        this.client.on('connect', () => {
            this.client.subscribe(this.brokerInfo.topic);
            console.log('broker connected');
        });

        this.client.on('message', (topic: string, message: Buffer) => {
            const automation: Automation = JSON.parse(message.toString());
            console.log(automation);
        });
    }
}
