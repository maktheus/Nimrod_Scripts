import sounddevice as sd
import serial
import numpy as np

SERIAL_PORT = 'COM3'
SERIAL_RATE = 500000
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
CHUNK = 1200


def readserial():
    data = []
    datax = []
    result = []
    while len(data) < CHUNK:
        raw_data = ser.readline().replace("\r\n", "").split(", ")

        if len(raw_data) > 1:
            int_raw_data = float(raw_data[0])
            int_raw_datax = float(raw_data[1])
            if raw_data[0] != '' and raw_data[0] is not None:
                if int_raw_data > 4000:
                    int_raw_data = 0
                try:
                    data.append(str(int_raw_data))
                    datax.append(str(int_raw_datax))
                except:
                    print ("loss")
        else:
            try:
                int_raw_data = float(raw_data[0])
            except:
                int_raw_data = 0.0
            if raw_data[0] != '' and raw_data[0] is not None:
                if int_raw_data > 4000:
                    int_raw_data = 0
                try:
                    data.append(str(int_raw_data))
                except:
                    print ("loss")
    result.append(np.array(data))
    result.append(np.array(datax))
    return result



res = readserial()
lines = res[0]

with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))

# for i in range(1200):
#     try:
#         if res[0][i] +1 != res[0][i+1]:
#             print (i)
#             print (res[0][i])
#             print (res[0][i+1])
#     except:
#         print ("erro")
#
# print("----------------------------------------------")
# for i in range(1200):
#
#     print (i)
#     print (res[0][i])