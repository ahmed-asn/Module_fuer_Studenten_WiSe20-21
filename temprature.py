from machine import Pin
from time import sleep
from onewire import OneWire
from ds18x20 import DS18X20

def read_temp(pin):
    ds_pin = Pin(pin)
    sensor = DS18X20(OneWire(ds_pin))

    roms = sensor.scan()
    print("DS Geräte:", roms)

    
    sensor = False
    i = 0
    while not sensor:
    
        if len(roms) != 0:
            return(sensor)

        else :
            print("Keine Sensoren gefunden! Schaltung kontrollieren, in kürze wird erneut gesucht...")
            i += 1
            if i > 2:
                   print("3 mal Fehlgeschlagen! Versuchen Sies später erneut.")
                   return(None)
            
            
    
