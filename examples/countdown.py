#!/usr/bin/env python

import sys
import time
import fourletterphat

print("""
Four Letter pHAT: countdown.py

This example will display a countdown.

Press Ctrl+C to exit.
""")

def safe_input(message):
    try:
        return raw_input(message)
    except NameError:
        return input(message)

mins, secs = 0, 0

while True:
    cd_time = safe_input('Enter a countdown time in MM:SS, e.g. "00:30" for 30 seconds: ')

    try:
        mins, secs = [float(x) for x in cd_time.strip('"').split(":")]
        break
    except ValueError:
        pass

start_time = time.time()
end_time = start_time + (mins * 60) + secs
run_time = end_time - start_time
curr_time = start_time

print("Counting down {mins} minutes and {secs} seconds...".format(mins=mins, secs=secs))

while curr_time < end_time:
    curr_time = time.time()
    remaining = end_time - curr_time
    hundredths = int(remaining * 100)

    if int(remaining) > 59:
        curr_mins = int(remaining / 60)
        curr_secs = int(remaining % 60)
        padded_str = str("{0:02d}".format(curr_mins)) + str("{0:02d}".format(curr_secs))
    else:
        curr_secs = int(remaining)
        curr_hundredths = int(remaining * 100 % 100)
        padded_str = str("{0:02d}".format(curr_secs)) + str("{0:02d}".format(curr_hundredths))

    fourletterphat.clear()
    fourletterphat.print_str(padded_str)
    fourletterphat.set_decimal(1, 1)
    fourletterphat.show()

spinner = ["|", "/", "-", "\\"]
fourletterphat.clear()

print("Done!")

while True:
    for i in range(4):
        for s in spinner:
            s = s * 4
            fourletterphat.clear()
            fourletterphat.print_str(s)
            fourletterphat.show()
            time.sleep(1 / 16.0)
