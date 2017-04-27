#!/usr/bin/env python

import time
import fourletterphat

print("""
Four Letter pHAT: demo.py

Displays a basic demo sequence.

Press Ctrl+C to exit.
""")


words = ["AHOY", "YARR", "GROG"]
spinner = ["|", "/", "-", "\\"]

while True:
    for w in words:
        fourletterphat.clear()
        fourletterphat.print_str(w)
        fourletterphat.show()
        time.sleep(1)
    for i in range(4):
        for s in spinner:
            s = s * 4
            fourletterphat.clear()
            fourletterphat.print_str(s)
            fourletterphat.show()
            time.sleep(1 / 16.0)
    for i in range(0,10000,25):
        fourletterphat.clear()
        fourletterphat.print_number_str(str(i))
        fourletterphat.show()
        time.sleep(1/10000.0)
