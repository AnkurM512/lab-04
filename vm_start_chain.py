import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import time
num = 5
while(True):
	publish.single("ankurmat/ping", num, hostname = "172.20.10.8")
	m = subscribe.simple("ankurmat/pong", hostname = "172.20.10.8")
	m2 = int(m.payload)+1
	print(m2)
	time.sleep(1)
	publish.single("ankurmat/ping", m2, hostname = "172.20.10.8")
