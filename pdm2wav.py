import sys
import wave

def pcm2wav(pcm_file, wav_file, channels=1, bits=16, sample_rate=16000):
    cnt = 0
    pcmdata_last='0000'
    pcmf = open(pcm_file, 'r')
    wavfile = wave.open(wav_file, 'wb')
    pcmdata_len = len(pcmf.read())
    pcmf.seek(0)
    
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    
    while cnt < pcmdata_len :
        #we only use the data which is in right length
        pcmdata = pcmf.readline()
        len_tmp = len(pcmdata)
        if len(pcmdata) == 5 :
            pcmdata = pcmdata[0:4]
            pcmdata_last = pcmdata
            temp = int(pcmdata, 16)
        else :
            temp = int(pcmdata_last, 16)
            
        wavfile.writeframes(temp.to_bytes(2, 'little'))
        cnt = cnt + len_tmp
        
    wavfile.close()
    pcmf.close()
    
if __name__ == '__main__':
    print("enter main")
    pcm2wav(sys.argv[1], sys.argv[2])
    print("success")
    