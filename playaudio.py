import sounddevice as sd
import serial
import numpy as np

SERIAL_PORT = 'COM7'
SERIAL_RATE = 115200
ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
CHUNK = 26000


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
                    data.append(int_raw_data)
                    datax.append(int_raw_datax)
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
                    data.append(int_raw_data)
                except:
                    print ("loss")
    result.append(np.array(data))
    result.append(np.array(datax))
    return result


while True:
    res = readserial()

    value = res[0]/max(res[0])
    value = value-np.mean(value)

    sd.play(value,10000  )
