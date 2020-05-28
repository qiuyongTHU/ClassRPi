import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
gpio = 18

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    time.sleep(5)
