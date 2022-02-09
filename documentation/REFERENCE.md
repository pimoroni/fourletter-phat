# Four Letter pHAT Function Reference

## Set A Single Digit

```python
fourletterphat.set_digit(pos, digit, decimal=False)
```
Set digit at position to provided value.

Position should be a value of 0 to 3 with 0 being the left most digit on the display.  
Digit should be any ASCII value 32-127 (printable ASCII).  

```python
fourletterphat.set_digit_raw(pos, bitmask)
```
Set digit at position to raw bitmask value.

Position should be a value of 0 to 3 with 0 being the left most digit on the display.

## Set A Decimal Point

```python
fourletterphat.set_decimal(pos, decimal)
```
Turn decimal point on or off at provided position.

Position should be a value 0 to 3 with 0 being the left most digit on the display.  
Decimal should be True to turn on the decimal point and False to turn it off.  

## Print A Float

```python
fourletterphat.print_float(value, decimal_digits=2, justify_right=True)
```
Print a numeric value to the display.

If value is negative it will be printed with a leading minus sign.  
Decimal digits is the desired number of digits after the decimal point.  

## Print Hexadecimal

```python
fourletterphat.print_hex(value, justify_right=True)
```
Print a numeric value in hexadecimal.

Value should be from 0 to FFFF.

## Print A String

```python
fourletterphat.print_str(value, justify_right=True)
```
Print a 4 character long string of values to the display.

Characters in the string should be any ASCII value 32 to 127 (printable ASCII).

## Print A Number String

```python
fourletterphat.print_number_str(value, justify_right=True)
```
Print a 4 character long string of numeric values to the display.

This function is similar to print_str but will interpret periods not as characters but as decimal points associated with the previous character.

## Blink The Display

```python
fourletterphat.set_blink(frequency)
```
Blink display at specified frequency.

Note that frequency must be a value allowed by the HT16K33, specifically one of:  
HT16K33_BLINK_OFF, HT16K33_BLINK_2HZ, HT16K33_BLINK_1HZ, or HT16K33_BLINK_HALFHZ.  

## Set Brightness

```python
fourletterphat.set_brightness(brightness)
```
Set brightness of entire display to specified value.

Supports 16 levels, from 0 to 15.

## Clear The Display
```python
fourletterphat.clear()
```
Clear contents of display buffer.

## Update The Display

Once you’ve made your changes, you’ll need to update the display.

```python
fourletterphat.show()
```
Display buffer on display.

## Glow The Display

Cycle display brightness from low to high and back to low.

```python
fourletterphat.glow(self, period=4, duration=4)
```
Cycle display brightness from low to high and back to low,
at a frequency of 1/periodicity Hz
and for a duration stated in seconds.
This function returns after duration seconds.
The periodicity acounts from initial brightness back to initial brightness.

## Scroll a message

Scroll a string on the display.

```python
fourletterphat.scroll_print(self, s, tempo=0.3)
```
Scroll a string on the display.
Display is paused 3xtempo seconds at the start,
then tempo seconds after each one character scroll,
then 3xtempo seconds at the end

## Flip the display

Write everything upside-down.

```python
fourletterphat.set_flipped()
```

Undo by calling set_flipped(False)

```python
fourletterphat.set_flipped(False)
```
