import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
import time
while(True):
	m = subscribe.simple("ankurmat/ping", hostname = "172.20.10.8")
	m2 = int(m.payload) + 1
	print(m2)
	time.sleep(1)
	publish.single("ankurmat/pong", m2, hostname = "172.20.10.8")
