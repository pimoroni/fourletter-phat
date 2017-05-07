#!/usr/bin/env python

import fourletterphat

print("""
Four Letter pHAT: glow.py

This example will glow a message at different speeds and durations.

Press Ctrl+C to exit.
""")

while True:
    fourletterphat.clear()
    fourletterphat.print_str("P1D4")
    fourletterphat.show()
    fourletterphat.glow(period=1, duration=4)

    fourletterphat.print_str("P4D8")
    fourletterphat.show()
    fourletterphat.glow(period=4, duration=8)