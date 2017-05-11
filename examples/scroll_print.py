#!/usr/bin/env python

import fourletterphat

print("""
Four Letter pHAT: scroll_print.py

This example will scroll a message at different speeds.

Press Ctrl+C to exit.
""")

while True:
    fourletterphat.clear()
    fourletterphat.scroll_print("DEFAULT SCROLLING SPEED")
    fourletterphat.scroll_print("1 SECOND PERIOD SCROLLING", 1)
    fourletterphat.scroll_print("1/10 SECOND PERIOD SCROLLING", 0.1)