#!/usr/bin/python3

from ABE_ExpanderPi import ADC
import time

"""
================================================
ABElectronics Expander Pi | ADC Read Demo
Version 1.0 Created 29/03/2015

run with: python3 demo-adcread.py
================================================

this demo reads the voltage from channel 1 on the ADC inputs
"""


adc = ADC()  # create an instance of the ADC

# set the reference voltage.  this should be set to the exact voltage
# measured on the Expander Pi Vref pin.
adc.set_adc_refvoltage(4.096)

while True:
    # read the voltage from channel 1 in single ended mode and display on the screen
    print (adc.read_adc_voltage(1, 0))
    time.sleep(0.5)
