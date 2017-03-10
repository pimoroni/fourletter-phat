#!/usr/bin/env python

import time
import fourletterphat as flp

while True:
    flp.clear()
    str_time = time.strftime("%H%M")
    flp.print_number_str(str_time)
    if int(time.time()) % 2 == 0:
        flp.set_decimal(1, 1)
    else:
        flp.set_decimal(1, 0)
    flp.show()
    time.sleep(0.1)
