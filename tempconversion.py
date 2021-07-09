#tempconversion.py
"""  Tempconversion function between fahrenheit and centigrade"""

#Functions

def to_centigrade(x):
    """ Returns x converted to centigrade"""
    return 5*(x-32)/9.0

def to_fahrenheit(x):
    """ Returns x converted to fahrenheit"""
    return 9*x/5.0+32
#constants

FREEZING_C=0.0    #water freezing temperature
FREZZING_F=32.0   #water freezing temperature

