# arduino-pulseaudio-controller

Very simple, very "boring" approach -- not fancy at all, but can be implemented very easily.

Only needs componets from the Arduino Starter Kit, and a bit of Python.

The approach is far from optimal, with the poller struggling to keep up with the serial input,
and unnecessarily issuing a lot more commands than needed. Also, everything is hardcoded...

If you'd like a robust, battle-tested approach, you should look at the excellent deej project:
https://github.com/omriharel/deej

## Parts
All included in the official Arduino UNO Starter Kit

- 1x Arduino UNO
- 3x Potentiometers
- 3x capacitors (100 μF) - may not be needed depending on the input's stability
- Assorted cables

## Drawings
Capacitors not pictured -- may not be necessary depending on how stable the input is.

![](https://gist.githubusercontent.com/marcolussetti/87fcdbd1edf1c4dd0673b2a1df2b7dd8/raw/e659a19eafd44a0aa08bae0d2e2d957d79caffbb/drawings.png?s=500)


## Schematics
Capacitors not pictured -- may not be necessary depending on how stable the input is.

![](https://gist.githubusercontent.com/marcolussetti/87fcdbd1edf1c4dd0673b2a1df2b7dd8/raw/e659a19eafd44a0aa08bae0d2e2d957d79caffbb/schematics.png?s=500)

## Code

- Arduino code (`print_potentiometer_values.ino`)
  - Very straightforward, if you got more potentiometers copy&paste sections or switch to a semi-decent code :)
- Python code (`poller.py`)
  - Customize the app mapping by altering the constants above. I used three pots:
    - One: things that play audio in the background -- Spotify, Firefox (for Twitch, Plex)
    - Two: things that play audio in the foreground -- Games
    - Three: meetings -- Discord, Chromium (for Teams in the browser, also Slack/Electron)
  - To target apps, easiest thing is `sink.proplist["application.name"]` as `name` is mostly useless. You could also get fancy and target by PID.

## Other stuff

- List current inputs by filter (`dev_poll_inputs.py`)
  - List pulsesecure sinks with their properties.
