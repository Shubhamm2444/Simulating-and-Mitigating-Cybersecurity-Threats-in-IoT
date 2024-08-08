Code Example: Setting Up MQTT Communication

import paho.mqtt.client as mqtt

# Define the MQTT settings
broker = "test.mosquitto.org"
port = 1883
topic = "iot/test"

# The callback function for when the client receives a message
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")

# Set up the MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic)
client.loop_start()

# Publish a test message
client.publish(topic, "Hello IoT")

# Run for a short time to allow message processing
import time
time.sleep(10)
client.loop_stop()
