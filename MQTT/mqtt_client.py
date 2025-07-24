import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883)
client.subscribe("robotic_arm/update")
client.on_message = on_message
client.loop_forever()