#!/usr/bin/env python

import time
import fourletterphat
from subprocess import Popen, PIPE

print("""
Four Letter pHAT: cpu-temp.py

This example will display your Pi's CPU
temperature in degrees celsius.

Press Ctrl+C to exit.
""")


while True:
    # Get temp forom vcgencmd in the format: "temp=XY.Z'C"
    # and reduce to the format "XYZC" for display
    temperature = Popen(["vcgencmd", "measure_temp"], stdout=PIPE)
    temperature = temperature.stdout.read().decode('utf-8')

    # Rempve "temp=" and the "." and "'" chars
    temperature = temperature[5:].replace(".", "").replace("'", "").strip()

    fourletterphat.clear()
    fourletterphat.print_str(temperature)
    fourletterphat.set_decimal(1, 1)
    fourletterphat.show()

    time.sleep(1)

