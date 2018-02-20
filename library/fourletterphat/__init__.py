import atexit
from sys import exit, version_info
from .i2c_bus import bus
from .alphanum4 import AlphaNum4
from .HT16K33 import *

__version__ = '0.1.0'


display = None

_is_setup = False


def _exit():
    display.clear()
    display.show()

def set_blink(frequency):
    """Blink display at specified frequency.

    Note that frequency must be a value allowed by the HT16K33, specifically one of:

     * HT16K33_BLINK_OFF,
     * HT16K33_BLINK_2HZ,
     * HT16K33_BLINK_1HZ, or
     * HT16K33_BLINK_HALFHZ.

    """

    setup()
    display.set_blink(frequency)

def set_brightness(brightness):
    """Set brightness of entire display to specified value.

    Supports 16 levels, from 0 to 15.

    """

    setup()
    display.set_brightness(brightness)

def set_digit_raw(pos, bitmask):
    """Set digit at position to raw bitmask value.

    Position should be a value of 0 to 3 with 0 being the left most digit on the display.

    """

    setup()
    display.set_digit_raw(pos, bitmask)

def set_decimal(pos, decimal):
    """Turn decimal point on or off at provided position.

    Position should be a value 0 to 3 with 0 being the left most digit on the display.
    Decimal should be True to turn on the decimal point and False to turn it off.

    """

    setup()
    display.set_decimal(pos, decimal)

def set_digit(pos, digit, decimal=False):
    """Set digit at position to provided value.

    Position should be a value of 0 to 3 with 0 being the left most digit on the display.
    Digit should be any ASCII value 32-127 (printable ASCII).

    """

    setup()
    display.set_digit(pos, digit, decimal)

def print_str(value, justify_right=True):
    """Print a 4 character long string of values to the display.

    Characters in the string should be any ASCII value 32 to 127 (printable ASCII).

    """

    setup()
    display.print_str(value, justify_right)

def print_number_str(value, justify_right=True):
    """Print a 4 character long string of numeric values to the display.

    This function is similar to print_str but will interpret periods not as
    characters but as decimal points associated with the previous character.

    """

    setup()
    display.print_number_str(value, justify_right=True)

def print_float(value, decimal_digits=2, justify_right=True):
    """Print a numeric value to the display.

    If value is negative it will be printed with a leading minus sign.
    Decimal digits is the desired number of digits after the decimal point.

    """

    setup()
    display.print_float(value, decimal_digits, justify_right)

def print_hex(value, justify_right=True):
    """Print a numeric value in hexadecimal.

    Value should be from 0 to FFFF.

    """

    setup()
    display.print_hex(value, justify_right)

def show():
    """Display buffer on display."""

    setup()
    display.show()

def clear():
    setup()
    display.clear()

def glow(period=4, duration=4):
    """Cycles display brightness from low to high and back to low,
    at a frequency of 1/period Hz and for a duration stated in seconds.

    The periodicity accounts from initial brightness back to initial brightness.

    :param period: Period of glow effect in seconds. (default 4 for 0.25Hz)
    :param duration: Duration of glow effect in seconds. Function returns after duration seconds (default 4 seconds)

    """

    setup()
    display.glow(period, duration)

def scroll_print(s, tempo=0.3):
    """Scrolls a string on the display.

       :param tempo: Display is paused 3xtempo seconds at the start,
         then tempo seconds after each one character scroll, then 3xtempo seconds at the end. (default 0.3 seconds)

    """

    setup()
    display.scroll_print(s, tempo)

def setup():
    """Set up the display."""

    global _is_setup, display

    if _is_setup:
        return True

    display = AlphaNum4(i2c=bus)
    display.begin()
    display.clear()
    display.show()

    atexit.register(_exit)

    _is_setup = True

