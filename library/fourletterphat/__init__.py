import atexit
from sys import exit, version_info
from .i2c_bus import bus
from .alphanum4 import AlphaNum4

__version__ = '0.0.1'

display = AlphaNum4(i2c=bus)
display.begin()
display.clear()
display.show()

set_digit_raw = display.set_digit_raw
set_decimal = display.set_decimal
set_digit = display.set_digit
print_str = display.print_str
print_number_str = display.print_number_str
print_float = display.print_float
print_hex = display.print_hex
show = display.show
clear = display.clear

def _exit():
    display.clear()
    display.show()

atexit.register(_exit)
