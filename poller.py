import time
import pulsectl

import serial

# Constants, map pot to applications
APPS_BY_POT = [
    [  # Music Pot
        "Spotify",
        "Firefox"
    ],
    [  # Foreground Pot
        "csgo_linux64",  # Counter-Strike: Global Offensive
        "FMOD Ex App",  # Mini Metro
    ],
    [  # Meetings Pot
        "WEBRTC VoiceEngine",  # Discord
        "Chromium",  # Slack (Electron), Teams (via Chromium browser), Webex (via Chromium Browser)
    ]
]


def process_input(line):
    command = line.decode().strip()
    try:
        pot, val = command.split("=")
    except:
        return "failure", 0.0
    relative = abs(1023-int(val))/1023
    if relative < 0:
        return "fail", 0
    elif relative > 1:
        return "fail", 1

    return pot, relative

def execute_pot(pulse, app_names, val):
    sinks = [sink for sink in pulse.sink_input_list()
             if sink.proplist["application.name"] in app_names]
    for sink in sinks:
        pulse.volume_set_all_chans(sink, val)


def main():
    pulse = pulsectl.Pulse('app-volume-ctl')
    for i in range(5):
        try:
            ser = serial.Serial(f"/dev/ttyACM{i}", timeout=5)
            print(f"Listening for commands on /dev/ttyACM{i}")
            break
        except:
            print(f"No device on /dev/ttyACM{i}")

    # Main loop
    while True:
        reading = ser.readline()
        pot, val = process_input(reading)
        if pot == "potOne":
            execute_pot(pulse, APPS_BY_POT[0], val)
        elif pot == "potTwo":
            execute_pot(pulse, APPS_BY_POT[1], val)
        elif pot == "potThree":
            execute_pot(pulse, APPS_BY_POT[2], val)

        if not ser.inWaiting():
            time.sleep(0.1)
        else:
            _ = ser.readline()  # Allows to catch up to input

if __name__ == "__main__":
    main()
