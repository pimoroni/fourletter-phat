#!/usr/bin/env python

import time
import fourletterphat as flp

words = ["AHOY", "YARR", "GROG"]
spinner = ["|", "/", "-", "\"]

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
            time.sleep(0.1)
