#!/usr/bin/env python

import time
import fourletterphat as flp

words = ["AHOY", "YARR", "GROG"]
spinner = ["|", "/", "-", "\\"]

while True:
    for w in words:
        flp.clear()
        flp.print_str(w)
        flp.show()
        time.sleep(1)
    for i in range(4):
        for s in spinner:
            s = s * 4
            flp.clear()
            flp.print_str(s)
            flp.show()
            time.sleep(1 / 16.0)
    for i in range(0,10000,25):
        flp.clear()
        flp.print_number_str(str(i))
        flp.show()
        time.sleep(1/10000.0)
