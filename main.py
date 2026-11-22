
import machine
import dht
import time

sensor = dht.DHT22(machine.Pin(15))
led = machine.Pin(16, machine.Pin.OUT)

while True:
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()

    if temperature >= 30:
        led.value(1)
        fan = "ON"
    elif temperature < 28:
        led.value(0)
        fan = "OFF"

    print("Temperature:", temperature, "C")
    print("Humidity:", humidity, "%")
    print("Fan:", fan)

    time.sleep(2)

    

