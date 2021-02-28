import time

import pulse

pulse = pulsectl.Pulse('app-volume-ctl2')

while True:
  for a in pulse.sink_input_list():
    print(a.proplist)
   print("===")
   time.sleep(1)