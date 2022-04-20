import sys

def get_sign16(vx):
    if vx <= 0x8000:
        return vx
    return vx - 0x10000

def pdm2txt(pdm_file, txt_file):
    cnt = 0
    temp_last='0'
    pcmf = open(pdm_file, 'r')
    txtf = open(txt_file, 'w')
    pcmdata_len = len(pcmf.read())
    pcmf.seek(0)
    
    while cnt < pcmdata_len :
        pcmdata = pcmf.readline()
        len_tmp = len(pcmdata)
        if len(pcmdata) == 5 :
            pcmdata = pcmdata[0:4]
            temp = int(pcmdata, 16)
            temp = get_sign16(temp)
            temp_last = temp
        else :
            temp = temp_last
        txtf.write(str(temp));
        txtf.write('\n')
        cnt = cnt + len_tmp
        
    txtf.close()
    pcmf.close()
    
if __name__ == '__main__':
    print("enter main")
    pdm2txt(sys.argv[1], sys.argv[2])
    print("success")