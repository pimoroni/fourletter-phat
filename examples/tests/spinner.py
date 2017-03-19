#!/usr/bin/env python

import time
import fourletterphat as flp

spinner = ["|", "/", "-", "\\"]

while True:
    for i in range(4):
        for s in spinner:
            s = s * 4
            flp.clear()
            flp.print_str(s)
            flp.show()
            time.sleep(0.1)
