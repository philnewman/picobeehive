import onewire, ds18x20, time
from machine import Pin

from lcd1602 import LCD
lcd=LCD()
lcd.clear() 

SensorPin = Pin(26, Pin.IN)
alert = Pin(15, Pin.OUT)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()
print(roms)
while True:
   sensor.convert_temp()
   time.sleep(2)
   lcd.clear()
   for rom in roms:
       temperature = round(sensor.read_temp(rom),1)
       temp_f = round(temperature * 9.0 / 5.0 + 32.0,2)
       if temperature >= 37.8:
           print("Warning the temperature is",temperature,"C ",temp_f,"F")
           for i in range(10):
               alert.toggle()
               time.sleep(0.5)
       else:
           print(temperature,"C")
           print(temp_f, "F")
           message = str(temperature) + " C"
           #lcd.message(message)
           lcd.write(0,0,message)
           message = str(temp_f) + " F"
           lcd.write(0,1,message)
           
time.sleep(5)
