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

## Schematic
In progress

## Code

- Arduino code
  - Very straightforward, if you got more potentiometers copy&paste sections or switch to a semi-decent code :)
- Python code
  - Customize the invocation/cluster in each of the pot execution methods. I used three pots:
    - One: things that play audio in the background -- Spotify, Firefox (for Twitch, Plex)
    - Two: things that play audio in the foreground -- Games
    - Three: meetings -- Discord, Chrome (for Teams), Slack, Telegram