#!/usr/bin/env python

import sys
import time
import fourletterphat as flp

def safe_input(message):
    try:
        return raw_input(message)
    except NameError:
        return input(message)

cd_time = safe_input('Enter a countdown time in MM:SS, e.g. "00:30" for 30 seconds: ')
mins, secs = [float(x) for x in cd_time.strip('"').split(":")]
start_time = time.time()
end_time = start_time + (mins * 60) + secs
run_time = end_time - start_time
curr_time = start_time

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

    flp.clear()
    flp.print_str(padded_str)
    flp.set_decimal(1, 1)
    flp.show()

spinner = ["|", "/", "-", "\\"]
flp.clear()

while True:
    for i in range(4):
        for s in spinner:
            s = s * 4
            flp.clear()
            flp.print_str(s)
            flp.show()
            time.sleep(1 / 16.0)
