import Serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
ser.write(b'Hello')
ser.close()