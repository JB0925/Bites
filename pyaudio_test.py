import pyaudio
import wave
import sys
import pitch

def read_and_write_audio():
    CHUNK = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100
    seconds = 3
    filename = 'test.wav'


    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate = fs,
                    frames_per_buffer=CHUNK,
                    input=True)

    frames = []

    for i in range(0, int(fs / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()


    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    return filename

def get_pitch(filename= read_and_write_audio()):
    #filename = read_and_write_audio()
    p = pitch.find_pitch(filename)
    print(f'pitch = {p}')


get_pitch()