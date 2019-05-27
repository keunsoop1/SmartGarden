# Import SDK packages
import json

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

topic_status = "smartgarden/status"
topic_watering = "smartgarden/watering"
topic_readings = "smartgarden/readings"
topic_max_data = "smartgarden/maxdata"

host = "arkau3u0cw2s4-ats.iot.eu-west-1.amazonaws.com"
rootCAPath = "certs/rootca.pem"
certificatePath = "certs/certificate.pem.crt"
privateKeyPath = "certs/private.pem.key"

# Stablishing MQTT Connection
my_rpi = AWSIoTMQTTClient("Raspbery_Core")
my_rpi.configureEndpoint(host, 8883)
my_rpi.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# mosquitto_sub -h arkau3u0cw2s4-ats.iot.eu-west-1.amazonaws.com -p 8883 -k 60 -i Raspberry_Core --cafile rootca.pem --cert certificate.pem.crt  --key private.pem.key -t 'smartgarden/readings' -d

my_rpi.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
my_rpi.configureDrainingFrequency(2)  # Draining: 2 Hz
my_rpi.configureConnectDisconnectTimeout(10)  # 10 sec
my_rpi.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
my_rpi.connect()


# Publish to the same topic in a loop forever
def publish_status(data):
    print('Publishing a message to {}: {}'.format(topic_status, data))
    my_rpi.publish(topic_status, json.dumps(data), 1)


def publish_watering(data):
    print('Publishing a message to {}: {}'.format(topic_watering, data))
    my_rpi.publish(topic_watering, json.dumps(data), 1)


def publish_readings(data):
    print('Publishing a message to {}: {}'.format(topic_readings, data))
    my_rpi.publish(topic_readings, json.dumps(data), 1)


def publish_max_data(data):
    print('Publishing a message to {}: {}'.format(topic_max_data, data))
    my_rpi.publish(topic_max_data, json.dumps(data), 1)