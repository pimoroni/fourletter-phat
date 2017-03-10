#!/usr/bin/env python

import time
import fourletterphat as flp

test_chars = ["****", "0000"]

while True:
    for char in test_chars:
        flp.clear()
        flp.print_str(char)
        flp.show()
        time.sleep(0.25)
    for i in range(4):
        flp.set_decimal(i, 1)
    flp.show()
    time.sleep(0.25)
