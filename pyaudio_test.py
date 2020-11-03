import pyaudio
import wave
import sys

CHUNK = 1024

p = pyaudio.PyAudio()
wf = wave.open(sys.argv[0], 'rb')

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getchannels(),
                rate = wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

