#!/usr/bin/env python

import time
import fourletterphat

print("""
Four Letter pHAT: blink.py

Demonstrate the display blinking at
the three available speeds.

Press Ctrl+C to exit.
""")

fourletterphat.clear()
fourletterphat.print_str("BLNK")
fourletterphat.show()

# Display each blinkt speed for 4 seconds
for blink_speed in [
        fourletterphat.HT16K33_BLINK_HALFHZ,
        fourletterphat.HT16K33_BLINK_1HZ,
        fourletterphat.HT16K33_BLINK_2HZ]:
    fourletterphat.set_blink(blink_speed)
    time.sleep(4)

fourletterphat.set_blink(fourletterphat.HT16K33_BLINK_OFF)

fourletterphat.print_str("BOOM")
fourletterphat.show()
time.sleep(1)
