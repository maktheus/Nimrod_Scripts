import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

SERIAL_PORT = 'COM3'
SERIAL_RATE = 500000
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
CHUNK = 300


def readserial():
    data = []
    while len(data) < CHUNK:
        raw_data = ser.readline().replace("\r\n", "")
        if raw_data != '' and raw_data is not None:
            try:
                print(raw_data)
                data.append(int(raw_data))
            except:
                lost = 0
    result = np.array(data, dtype='b') + 127
    return result


while True:
    res = readserial()
    plt.show()
    print (res)
