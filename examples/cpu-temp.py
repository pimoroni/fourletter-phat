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


temps = []

while True:
    temp = Popen(["vcgencmd", "measure_temp"], stdout=PIPE)
    temp = temp.stdout.read().decode('utf-8')
    temp = temp[5:].replace(".", "").replace("'","").strip()
    fourletterphat.clear()
    fourletterphat.print_str(temp)
    fourletterphat.set_decimal(1, 1)
    fourletterphat.show()
    time.sleep(1)
