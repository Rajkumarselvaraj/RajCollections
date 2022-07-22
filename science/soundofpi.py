def make_pi(nod):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    #for j in range(nod):
    cnt=1
    while cnt <= nod:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
            cnt +=1

        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2



def getArrayofPi(nod):
    my_array = []   
    for i in make_pi(nod):
        my_array.append(i)
    print("my_array",my_array)
    return my_array

nod = 10000
pi_nums = getArrayofPi(nod)
print(pi_nums)
pi_nums2 = pi_nums[:1] + ['.'] + pi_nums[1:]
big_string = "".join([str(z) for z in pi_nums2])
print(big_string) 

#add sound to it


import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second
amplitude = 2
num_samples_lst = range(nod) 
sampling_rate = nod

file = "./Others/science/testPI.wav"
wav_file=wave.open(file, 'w')

nframes=nod

comptype="NONE"

compname="not compressed"

nchannels=1

sampwidth=2

wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

print(len(num_samples_lst),len(pi_nums))

for a,s in zip(num_samples_lst,pi_nums):
    #print(s,"->",struct.pack('h', int(s*amplitude)),"->",a,":",int(s*amplitude))
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))

plt.scatter(num_samples_lst, pi_nums)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()



