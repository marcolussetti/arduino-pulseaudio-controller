import logging
import time

import pulsectl
import serial

# Threshold to avoid changing too much
PRECISION_MULTIPLIER = 0.025
PRECISION = 3

# Map pots to applications
APPS_BY_POT = [
    [  # Music Pot
        "Spotify",
        "Firefox"
    ],
    [  # Foreground Pot
        "csgo_linux64",  # Counter-Strike: Global Offensive
        "StarCraft II (Retail)",
        "FMOD Ex App",  # Mini Metro
    ],
    [  # Meetings Pot
        "WEBRTC VoiceEngine",  # Discord
        "Chromium",  # Slack (Electron), Teams (via Chromium browser), Webex (via Chromium Browser)
    ]
]

# Store previous pot values to avoid double calling pulse
pot_values = [
    0,
    0,
    0
]


def process_input(line):
    command = line.decode().strip()
    try:
        pot_str, val = command.split("=")
        if not pot_str.startswith("pot"):
            raise AttributeError(f"Invalid pot: {pot_str}")
        pot = int(pot_str[3:])

        relative = abs(1023-int(val))/1023

        # Round to threshold
        relative_adj = round(PRECISION_MULTIPLIER * round(float(relative) / PRECISION_MULTIPLIER),
                             PRECISION)

        if relative < 0:
            raise OverflowError(f"Invalid value: {pot}")
        if relative > 1:
            raise OverflowError(f"Invalid value: {pot}")
    except Exception as e:
        logging.error(e)
        return "fail", 0

    return pot, relative_adj

def execute_pot(pulse, app_names, val):
    sinks = [sink for sink in pulse.sink_input_list()
             if sink.proplist["application.name"] in app_names]
    for sink in sinks:
        pulse.volume_set_all_chans(sink, val)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

    pulse = pulsectl.Pulse('app-volume-ctl')
    for i in range(10):
        try:
            ser = serial.Serial(f"/dev/ttyACM{i}", timeout=5)
            logging.info(f"Listening for commands on /dev/ttyACM{i}")
            break
        except:
            logging.info(f"No device on /dev/ttyACM{i}")

    # Main loop
    while True:
        reading = ser.readline()
        pot, val = process_input(reading)
        if pot != "fail" and val != pot_values[pot]:
            logging.debug(f"Pot {pot}: {pot_values[pot]} => {pot}")
            pot_values[pot] = val
            execute_pot(pulse, APPS_BY_POT[pot], val)

        if not ser.inWaiting():
            time.sleep(0.1)
        else:
            _ = ser.readline()  # Allows to catch up to input

if __name__ == "__main__":
    main()
