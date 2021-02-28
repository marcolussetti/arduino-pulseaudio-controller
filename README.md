# arduino-pulseaudio-controller

Very simple, very "boring" approach -- not fancy at all, but can be implemented very easily.

Only needs componets from the Arduino Starter Kit, and a bit of Python.

The approach is far from optimal, with the poller struggling to keep up with the serial input,
no config options, and so on :)

If you'd like a robust, battle-tested approach, you should look at the excellent deej project:
https://github.com/omriharel/deej


## Parts
All included in the official Arduino UNO Starter Kit

- 1x Arduino UNO
- 3x Potentiometers
- 3x capacitors (100 μF) - may not be needed depending on the input's stability.
- Assorted cables


## Code

- Arduino code (`print_potentiometer_values/print_potentiometer_values.ino`)
  - Very straightforward I think, if you have more potentiometers just increment the array sizes
- Python code (`poller.py`)
  - Customize the app mapping by altering the constants above. I used three pots:
    - One: things that play audio in the background -- Spotify, Firefox (for Twitch, Plex)
    - Two: things that play audio in the foreground -- Games
    - Three: meetings -- Discord, Chromium (for Teams in the browser, also Slack/Electron)
  - To target apps, easiest thing is `sink.proplist["application.name"]` as `name` is mostly useless. You could also get fancy and target by PID.
- Misc
  - List current inputs by filter (`dev_poll_inputs.py`)
    - List pulsesecure sinks with their properties.


## Drawings
Capacitors not pictured -- may not be necessary depending on how stable the input is.

![](/images/drawings.png?raw=true)


## Schematics
Capacitors not pictured -- may not be necessary depending on how stable the input is.

![](/images/schematics.png?raw=true)

## Finished work

![](/images/finished.jpg?raw=true)


## License

Copyright (c) 2021 Marco Lussetti.

Licensed under the terms of the Apache License 2.0.
