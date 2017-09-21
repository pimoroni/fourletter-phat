# This file was borrowed from https://github.com/adafruit/Adafruit_Python_LED_Backpack
# Original copyright included below:
# <3 @ Adafruit
#
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from . import HT16K33
import time


# Digit value to bitmask mapping:
DIGIT_VALUES = {
    ' ': 0b0000000000000000,
    '!': 0b0000000000000110,
    '"': 0b0000001000100000,
    '#': 0b0001001011001110,
    '$': 0b0001001011101101,
    '%': 0b0000110000100100,
    '&': 0b0010001101011101,
    '\'': 0b0000010000000000,
    '(': 0b0010010000000000,
    ')': 0b0000100100000000,
    '*': 0b0011111111000000,
    '+': 0b0001001011000000,
    ',': 0b0000100000000000,
    '-': 0b0000000011000000,
    '.': 0b0000000000000000,
    '/': 0b0000110000000000,
    '0': 0b0000110000111111,
    '1': 0b0000000000000110,
    '2': 0b0000000011011011,
    '3': 0b0000000010001111,
    '4': 0b0000000011100110,
    '5': 0b0010000001101001,
    '6': 0b0000000011111101,
    '7': 0b0000000000000111,
    '8': 0b0000000011111111,
    '9': 0b0000000011101111,
    ':': 0b0001001000000000,
    ';': 0b0000101000000000,
    '<': 0b0010010000000000,
    '=': 0b0000000011001000,
    '>': 0b0000100100000000,
    '?': 0b0001000010000011,
    '@': 0b0000001010111011,
    'A': 0b0000000011110111,
    'B': 0b0001001010001111,
    'C': 0b0000000000111001,
    'D': 0b0001001000001111,
    'E': 0b0000000011111001,
    'F': 0b0000000001110001,
    'G': 0b0000000010111101,
    'H': 0b0000000011110110,
    'I': 0b0001001000000000,
    'J': 0b0000000000011110,
    'K': 0b0010010001110000,
    'L': 0b0000000000111000,
    'M': 0b0000010100110110,
    'N': 0b0010000100110110,
    'O': 0b0000000000111111,
    'P': 0b0000000011110011,
    'Q': 0b0010000000111111,
    'R': 0b0010000011110011,
    'S': 0b0000000011101101,
    'T': 0b0001001000000001,
    'U': 0b0000000000111110,
    'V': 0b0000110000110000,
    'W': 0b0010100000110110,
    'X': 0b0010110100000000,
    'Y': 0b0001010100000000,
    'Z': 0b0000110000001001,
    '[': 0b0000000000111001,
    '\\': 0b0010000100000000,
    ']': 0b0000000000001111,
    '^': 0b0000110000000011,
    '_': 0b0000000000001000,
    '`': 0b0000000100000000,
    'a': 0b0001000001011000,
    'b': 0b0010000001111000,
    'c': 0b0000000011011000,
    'd': 0b0000100010001110,
    'e': 0b0000100001011000,
    'f': 0b0000000001110001,
    'g': 0b0000010010001110,
    'h': 0b0001000001110000,
    'i': 0b0001000000000000,
    'j': 0b0000000000001110,
    'k': 0b0011011000000000,
    'l': 0b0000000000110000,
    'm': 0b0001000011010100,
    'n': 0b0001000001010000,
    'o': 0b0000000011011100,
    'p': 0b0000000101110000,
    'q': 0b0000010010000110,
    'r': 0b0000000001010000,
    's': 0b0010000010001000,
    't': 0b0000000001111000,
    'u': 0b0000000000011100,
    'v': 0b0010000000000100,
    'w': 0b0010100000010100,
    'x': 0b0010100011000000,
    'y': 0b0010000000001100,
    'z': 0b0000100001001000,
    '{': 0b0000100101001001,
    '|': 0b0001001000000000,
    '}': 0b0010010010001001,
    '~': 0b0000010100100000
}


class AlphaNum4(HT16K33.HT16K33):
    """Alphanumeric 14 segment LED backpack display."""

    def __init__(self, **kwargs):
        """Initialize display.

        All arguments will be passed to the HT16K33 class initializer,
        including optional I2C address and bus number parameters.

        """

        super(AlphaNum4, self).__init__(**kwargs)

    def set_digit_raw(self, pos, bitmask):
        """Set digit at position to raw bitmask value.

        Position should be a value of 0 to 3 with 0 being the left most digit on the display.

        """

        if pos < 0 or pos > 3:
            # Ignore out of bounds digits.
            return
        # Set the digit bitmask value at the appropriate position.
        # Also set bit 7 (decimal point) if decimal is True.
        self.buffer[pos*2]   = bitmask & 0xFF
        self.buffer[pos*2+1] = (bitmask >> 8) & 0xFF

    def set_decimal(self, pos, decimal):
        """Turn decimal point on or off at provided position.

        Position should be a value 0 to 3 with 0 being the left most digit on the display.
        Decimal should be True to turn on the decimal point and False to turn it off.

        """

        if pos < 0 or pos > 3:
            # Ignore out of bounds digits.
            return
        # Set bit 14 (decimal point) based on provided value.
        if decimal:
            self.buffer[pos*2+1] |= (1 << 6)
        else:
            self.buffer[pos*2+1] &= ~(1 << 6)

    def set_digit(self, pos, digit, decimal=False):
        """Set digit at position to provided value.

        Position should be a value of 0 to 3 with 0 being the left most digit on the display.
        Digit should be any ASCII value 32-127 (printable ASCII).

        """

        self.set_digit_raw(pos, DIGIT_VALUES.get(str(digit), 0x00))
        if decimal:
            self.set_decimal(pos, True)

    def print_str(self, value, justify_right=True):
        """Print a 4 character long string of values to the display.

        Characters in the string should be any ASCII value 32 to 127 (printable ASCII).

        """

        # Left or right justify string according to justify_right parameter
        if justify_right:
            value = value.rjust(4, ' ')
        else:
            value = value.ljust(4, ' ')

        # Go through each character and print it on the display.
        for i, ch in enumerate(value):
            self.set_digit(i, ch)

    def print_number_str(self, value, justify_right=True):
        """Print a 4 character long string of numeric values to the display.

        This function is similar to print_str but will interpret periods not as
        characters but as decimal points associated with the previous character.

        """

        value = str(value)

        # Calculate length of value without decimals.
        length = len(value.replace(".",""))

        # Error if value without decimals is longer than 4 characters.
        if length > 4:
            raise ValueError("Number '{}' is too large to display".format(value))

        # Left or right justify string according to justify_right parameter
        # Extra justification is added for any decimal places which don't take up a char slot
        pos = 0

        justify_length = len(value) - length

        if justify_right:
            value = value.rjust(4 + justify_length, ' ')
        else:
            value = value.ljust(4 + justify_length, ' ')

        # Go through each character and print it on the display.
        for i, ch in enumerate(value):
            if ch == '.':
                # Print decimal points on the previous digit.
                self.set_decimal(pos-1, True)
            else:
                self.set_digit(pos, ch)
                pos += 1

    def print_float(self, value, decimal_digits=2, justify_right=True):
        """Print a numeric value to the display.

        If value is negative it will be printed with a leading minus sign.
        Decimal digits is the desired number of digits after the decimal point.

        """

        format_string = '{{0:0.{0}F}}'.format(decimal_digits)
        self.print_number_str(format_string.format(value), justify_right)

    def print_hex(self, value, justify_right=True):
        """Print a numeric value in hexadecimal.

        Value should be from 0 to FFFF.

        """

        if value < 0 or value > 0xFFFF:
            # Ignore out of range values.
            return
        self.print_str('{0:X}'.format(value), justify_right)

    def show(self):
        """Display buffer on display."""

        self.write_display()

    def glow(self, period=4, duration=4):
        """Cycles display brightness from low to high and back to low,
        at a frequency of 1/period Hz and for a duration stated in seconds.
        The periodicity accounts from initial brightness back to initial brightness.
        :param period: Period of glow effect in seconds. (default 4 for 0.25Hz) 
        :param duration: Duration of glow effect in seconds. Function returns after duration seconds (default 4 seconds)

        """

        period = float(period)
        duration = float(duration)

        NB_OF_BRIGHTNESSES = 16
        MIN_BRIGHTNESS = 0
        MAX_BRIGHTNESS = NB_OF_BRIGHTNESSES - 1

        initial_brightness = self.get_brightness()
        current_brightness = initial_brightness

        nb_of_transitions = (NB_OF_BRIGHTNESSES-1)*2
        wait_between_transitions = period / nb_of_transitions
        time_left = duration
        adjustment = 1
        while time_left > 0:
            if current_brightness == MAX_BRIGHTNESS:
                # Once we reach max brightness, we go down
                adjustment = -1
            elif current_brightness == MIN_BRIGHTNESS:
                # Once we reach min brightness, we go up
                adjustment = 1

            current_brightness += adjustment   
            self.set_brightness(current_brightness)

            time.sleep(wait_between_transitions)
            time_left -= wait_between_transitions

        self.set_brightness(initial_brightness)

    def scroll_print(self, s, tempo=0.3):
        """Scrolls a string on the display.
           
           :param tempo: Display is paused 3xtempo seconds at the start,
             then tempo seconds after each one character scroll, then 3xtempo seconds at the end. (default 0.3 seconds)

        """

        length = len(s)
        # No need to scroll if the message is not bigger than the display
        if length <= 4:
            self.print_str(s)
            self.show()
        else:
            # Display the message start a bit longer
            self.print_str(s[0] + s[1] + s[2] + s[3])
            self.show()
            time.sleep(tempo * 3)

            for i in range(3, length):
                self.print_str(s[i - 3] + s[i - 2] + s[i - 1] + s[i])
                self.show()
                time.sleep(tempo)

        # Display the message end a bit longer
        time.sleep(tempo * 3)
