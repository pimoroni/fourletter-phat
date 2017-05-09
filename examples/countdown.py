#!/usr/bin/env python

import time
import fourletterphat

print("""
Four Letter pHAT: countdown.py

This example will display a countdown.

Press Ctrl+C to exit.
""")

# Try to use Python 2s safe `raw_input`,
# otherwise assume Python 3 `input`.
def safe_input(message):
    try:
        return raw_input(message)
    except NameError:
        return input(message)

minutes = 0
seconds = 0

# Loop until the user has entered a valid time
while True:
    cd_time = safe_input('Enter a countdown time in MM:SS, e.g. "00:30" for 30 seconds: ')

    try:
        # Very crudely parse out the minutes and seconds by splitting
        # on the ":" and casting the two parts to ints.
        minutes, seconds = [int(x) for x in cd_time.strip('"').split(":")]
        break
    except ValueError:
        # Any error parsing the users chosen time is ignored,
        # and we ask them to input a value again
        pass

# Calculate how long we need to count down for in seconds
start_time = time.time()
end_time = start_time + (minutes * 60) + seconds
run_time = end_time - start_time
curr_time = start_time

print("Counting down {minutes} minutes and {seconds} seconds...".format(minutes=minutes, seconds=seconds))

while curr_time < end_time:
    curr_time = time.time()
    remaining = end_time - curr_time
    hundredths = int(remaining * 100)

    # If greater than 59 seconds are left, display minutes + seconds
    if int(remaining) > 59:
        curr_minutes = int(remaining / 60.0)
        curr_seconds = int(remaining % 60)
        padded_str = str("{0:02d}".format(curr_minutes)) + str("{0:02d}".format(curr_seconds))

    # Otherwise display seconds + hundreths of a second
    else:
        curr_seconds = int(remaining)
        curr_hundredths = int(remaining * 100 % 100)
        padded_str = str("{0:02d}".format(curr_seconds)) + str("{0:02d}".format(curr_hundredths))

    fourletterphat.clear()
    fourletterphat.print_str(padded_str)
    fourletterphat.set_decimal(1, 1)
    fourletterphat.show()

spinner = ["|", "/", "-", "\\"]

fourletterphat.clear()

print("Done!")

# Display a brief spinner animation to indicate the countdown is complete
while True:
    for i in range(4):
        for s in spinner:
            s = s * 4
            fourletterphat.clear()
            fourletterphat.print_str(s)
            fourletterphat.show()
            time.sleep(1 / 16.0)
