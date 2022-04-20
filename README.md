# Debug tools for PDM Microphone on mcu

---

## Description
When we want to use the PDM mic with a mcu. We need a tool to convert the original data of mic to the audio file that we can use. 

***HERE IT IS***

---

## Tools Usage
### pdm2wav.py
We use it to convert the raw data of PDM to wav file.

Example:
```
python pdm2wav.py pdm-origin-data.txt pdm-audio.wav
```

***ATTENTION:***

Before this, we need to get the data from MCU. Usually we use the uart to get the data. And you can get the demo raw data from [here](https://github.com/bigbearishappy/mcu_pdm_debug_tools/blob/main/testdata/pdm-origintxt.txt)

You can use the following demo code to output the raw data
```
for(int i = 0;i < pdm_data_len; ++i)
    Serial.printf("%04x\n", pdm_data[i]);
```

### pdm2txt.py
Sometimes, we find that the PDM mic not work well as we want. And now we can take a look into the waveform of the PDM mic raw data.

Example:
```
python pdm2txt.py pdm-origin-data.txt pdm-waveform.txt
```

And we can use pdm2txt.py to convert the raw data to a float data. This can help us draw the waveform easily in excel.

Here is a demo waveform picture of PDM:

![image]( https://github.com/bigbearishappy/mcu_pdm_debug_tools/blob/main/pic/excel_data_analysis.png)

### wav2pdm.py
If we want ot get the PDM raw data from a wav file.We can use the wav2pdm.py.

Example:
```
python wav2pdm.py test.wav pdm-raw.bin
```

