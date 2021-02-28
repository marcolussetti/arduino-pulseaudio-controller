import time
import pulsectl

import serial


def process_input(line):
    command = line.decode().strip()
    try:
        pot, val = command.split("=")
    except:
        return "failure", 0.0
    relative = abs(1023-int(val))/1023

    return pot, relative

 
# Music pot
def execute_pot_one(pulse, val):
#     sts = Popen(f"playerctl --player=spotify volume {val}", shell=True).wait()
    spotify_sinks = [sink for sink in pulse.sink_input_list() if sink.name == "Spotify" or sink.proplist["application.name"] == "Firefox"]
    for sink in spotify_sinks:
        pulse.volume_set_all_chans(sink, val)


# Foreground entertainment pot
def execute_pot_two(pulse, val):
    gaming_sink_names = []
    gaming_sink_app_names = ["csgo_linux64"]
    game_sinks = [sink for sink in pulse.sink_input_list() if sink.name in gaming_sink_names or sink.proplist["application.name"] in gaming_sink_app_names]
    for sink in game_sinks:
        pulse.volume_set_all_chans(sink, val)


 # Foreground entertainment pot
def execute_pot_two(pulse, val):
    gaming_sink_names = []
    gaming_sink_app_names = ["csgo_linux64"]
    game_sinks = [sink for sink in pulse.sink_input_list() if sink.name in gaming_sink_names or sink.proplist["application.name"] in gaming_sink_app_names]
    for sink in game_sinks:
        pulse.volume_set_all_chans(sink, val)


# Meetings pot
def execute_pot_three(val):
    meeting_sink_names = []
    meeting_sink_app_names = ["WEBRTC VoiceEngine", "Chromium"]
    game_sinks = [sink for sink in pulse.sink_input_list() if sink.name in meeting_sink_names or sink.proplist["application.name"] in meeting_sink_app_names]
    for sink in game_sinks:
        pulse.volume_set_all_chans(sink, val)


def main():
  pulse = pulsectl.Pulse('app-volume-ctl', timeout=5)
  ser = serial.Serial('/dev/ttyACM0')

  # Clear log
  while ser.inWaiting():
      temp = ser.readline()

  while True:
      reading = ser.readline()
      pot, val = process_input(reading)
      if pot == "potOne":
          execute_pot_one(pulse, val)
      elif pot == "potTwo":
          execute_pot_two(pulse, val)
      elif pot == "potThree":
          execute_pot_three(pulse, val)

      if not ser.inWaiting():
          time.sleep(0.1)
      else:
          ser.readline()
          
if __name__ == "__main__":
  main()