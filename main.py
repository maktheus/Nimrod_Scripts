import numpy as np  # importing Numpy with an alias np
import pyaudio as pa
import matplotlib.pyplot as plt
import serial

# quantidade de samples por frame
CHUNK = 25000 * 1

SERIAL_PORT = 'COM7'
SERIAL_RATE = 115200

ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

fig, (ax, ax1) = plt.subplots(2)

x = np.arange(0, 2 * CHUNK, 2)

line, = ax.plot(x, np.random.rand(CHUNK), 'r')
line_fft, = ax1.plot(x, np.random.rand(CHUNK), 'b')

# Tamanho da visualizacao do grafico 1
ax.set_ylim(-2, 2)
ax.set_xlim = (0, CHUNK)

# Tamanho da visualizacao do grafico 2
ax1.set_xlim(0, CHUNK * 2)
ax1.set_ylim(0, 10)

fig.show()

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
                if int_raw_data > 10000:
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
                if int_raw_data > 10000:
                    int_raw_data = 0
                try:
                    data.append(int_raw_data)
                except:
                    print ("loss")
    result.append(np.array(data))
    result.append(np.array(datax))
    return result

while 1:
    data = readserial()

    raw_data = ser.readline().replace("\r\n", "").split(", ")
    if len(raw_data) > 1:
        value = data[0] - np.mean(data[0])
        valuex = data[1] - np.mean(data[1])
        line.set_ydata(value)
        line_fft.set_ydata(valuex)
        fig.canvas.draw()
        fig.canvas.flush_events()
    else:
        value = data[0]/max(data[0])
        value = value-np.mean(value)

        line.set_ydata(value)
        fig.canvas.draw()
        fig.canvas.flush_events()