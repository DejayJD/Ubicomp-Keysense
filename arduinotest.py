import serial
import time
import struct
import re
import numpy as np

serial_port = serial.Serial('COM4', baudrate=115200, timeout=1)
serial_port.flush()

def clean_data(data):
    data = data.split("s")
    cleaned_data = []
    for val in data:
        if val.count(',') == 3:
            values = val.split(',')
            for v in values:
                re.sub('[^0-9.]','',v)
            cleaned_data.append(values)
    return cleaned_data

total_data = ""
start = time.time()
while time.time()-start < 180:
    values = serial_port.read(500)
    total_data += values
    time.sleep(0.01)

    # if values:
    #     tmp = np.array([(value) for value in values])
    #     print tmp
        # print(tmp.astype(np.int16))

cleaned_data = clean_data(total_data)
print "Values recorded: " + str(len(cleaned_data))
# print cleaned_data
final_data = np.array(cleaned_data)
np.save("MaggieStressed.npy", final_data)
