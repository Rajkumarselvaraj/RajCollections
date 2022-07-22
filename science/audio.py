import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second

frequency = 100#1000

num_samples = 4800#0

# The sampling rate of the analog to digital convert

sampling_rate = 4800#0.0

amplitude = 16000

num_samples_lst = range(num_samples) 

file = "./Others/science/test.wav"
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in num_samples_lst]
wav_file=wave.open(file, 'w')

nframes=num_samples

comptype="NONE"

compname="not compressed"

nchannels=1

sampwidth=2

wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

for a,s in zip(num_samples_lst,sine_wave):
    print(s,"->",struct.pack('h', int(s*amplitude)),"->",a,":",int(s*amplitude))
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))

plt.plot(num_samples_lst, sine_wave)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()



