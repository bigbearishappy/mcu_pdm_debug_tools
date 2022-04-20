import sys
import numpy as np
def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype= data_type)
    data.tofile(pcmfile)
    
if __name__ == '__main__':
    print("enter main")
    wav2pcm(sys.argv[1], sys.argv[2])
    print("success")