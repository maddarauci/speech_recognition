'''
PyAudio: play a wave file (callback version)
'''

import pyaudio
import wave
import time, sys

if len(sys.argv) < 2:
    print("plays a wave file.\n\nUsage: %s filename.wave" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb') # read only

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# define callback
def callback(in_data, frame_count, time_infor, status):
    data = wf.readframe(frame_count)
    return (data, pyaudio.paContinue)

# open stream using callback
stream = p.open(format=p.get_format_from_width(wf.getsamplewidth()),
    channels = wf.getchannels(),
    rate= wf.getframerate(),
    output = True,
    stream_callback =callback
)



print('all good here')
