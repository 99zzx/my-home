import random


from paho.mqtt import client as mqtt_client
import threading
from window import *

broker = '116.62.62.25'
port = 1883
topic = "/ESP32_1aa73514/topic/post"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'



def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            #var.set('Connected to MQTT Broker!')
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        show_str(msg.payload.decode()[2:-2])
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

thread1 = run()
thread2 = my_window()

# 开启新线程


if __name__ == '__main__':
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()