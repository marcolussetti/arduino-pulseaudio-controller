# Control PulseAudio app volume with Arduino & a very dumb script

Yes the code is utter crap. No, I don't really care.
This is designed as the simplest, most dumb way of doing this. It allows for validation of the need for building a fully fledged thing.

If you want to actually use this, you should probably use a fully fledged project like the excellent https://github.com/omriharel/deej

## Parts
All included in the official Arduino UNO Starter Kit

- 1x Arduino UNO
- 3x Potentiometers
- 3x capacitors (100 μF)
- Assorted cables

## Drawings
In progress

## Schematics

## Code

- Arduino code (`print_potentiometer_values.ino`)
  - Very straightforward, if you got more potentiometers copy&paste sections or switch to a semi-decent code :)
- Python code (`poller.py`)
  - Customize the invocation/cluster in each of the pot execution methods. I used three pots:
    - One: things that play audio in the background -- Spotify, Firefox (for Twitch, Plex)
    - Two: things that play audio in the foreground -- Games
    - Three: meetings -- Discord, Chromium (for Teams in the browser, also Slack/Electron)
  - To target apps, easiest thing is `sink.proplist["application.name"]` as `name` is mostly useless. You can also do some more fancy things where you target by process id, and go look up your application that way

## Other stuff

- List current inputs by filter (`dev_poll_inputs.py`)
  - List pulsesecure sinks with their properties.