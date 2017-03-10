#!/usr/bin/env python

import time
import fourletterphat as flp
from subprocess import Popen, PIPE

while True:
    temp = Popen(["vcgencmd", "measure_temp"], stdout=PIPE)
    temp = temp.stdout.read()
    temp = temp[5:].replace(".", "").replace("'","").strip()
    flp.clear()
    flp.print_str(temp)
    flp.set_decimal(1, 1)
    flp.show()
    time.sleep(0.05)
