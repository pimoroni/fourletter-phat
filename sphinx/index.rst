.. role:: python(code)
   :language: python

.. toctree::
   :titlesonly:
   :maxdepth: 0

.. module:: fourletterphat

Welcome
-------

This documentation will guide you through the methods available in the Four Letter pHAT python library.

Four Letter pHAT is a Raspberry Pi add-on with four star displays.

* More information - https://shop.pimoroni.com/products/four-letter-phat
* GPIO Pinout - http://pinout.xyz/pinout/four_letter_phat
* Get the code - https://github.com/pimoroni/four-letter-phat
* Get help - http://forums.pimoroni.com/c/support

At A Glance
-----------

.. autoclassoutline:: fourletterphat.AlphaNum4
   :members:
   :inherited-members:

.. toctree::
   :titlesonly:
   :maxdepth: 0

Set A Single Digit
------------------

.. automethod:: fourletterphat.display.set_digit

.. automethod:: fourletterphat.display.set_digit_raw


Set A Decimal Point
-------------------

.. automethod:: fourletterphat.display.set_decimal

Print A Float
-------------

.. automethod:: fourletterphat.display.print_float

Print Hexadecimal
-----------------

.. automethod:: fourletterphat.display.print_hex

Print A String
--------------

.. automethod:: fourletterphat.display.print_str

Print A Number String
---------------------

.. automethod:: fourletterphat.display.print_number_str

Blink The Display
-----------------

.. automethod:: fourletterphat.display.set_blink

Set Brightness
--------------

.. automethod:: fourletterphat.display.set_brightness

Clear The Display
-----------------

.. automethod:: fourletterphat.display.clear

Update The Display
------------------

Once you've made your changes, you'll need to update the display.

.. automethod:: fourletterphat.display.show
