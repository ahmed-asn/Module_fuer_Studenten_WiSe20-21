from machine import Pin
from time import sleep
from onewire import OneWire
from ds18x20 import DS18X20

def temp(pin):
    ds_pin = Pin(pin)
    sensor = DS18X20(OneWire(ds_pin))

    roms = sensor.scan()
 
    if len(roms) != 0:
        return sensor.read_temp(roms[0])
    else:
        return None
        

    
