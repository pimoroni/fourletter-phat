#!/usr/bin/env python

import time
import fourletterphat

print("""
Four Letter pHAT: clock.py

This example will display a simple HH/MM clock,
with a blinking decimal point to indicate seconds.

Press Ctrl+C to exit.
""")

while True:
    fourletterphat.clear()

    str_time = time.strftime("%H%M")

    # Display the time
    fourletterphat.print_number_str(str_time)

    # Blink the middle decimal point
    # int(time.time() % 2) will alternate 1 0 1 0
    # which we can use to directly set the point
    fourletterphat.set_decimal(1, int(time.time() % 2))

    fourletterphat.show()
    time.sleep(0.1)
