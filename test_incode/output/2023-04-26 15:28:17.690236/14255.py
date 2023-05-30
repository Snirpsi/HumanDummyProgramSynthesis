#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or enumerates all ports. """    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM%s' % (i+1) for i in range(256)]
    
    for port in ports:
        try:
            ser = serial.Serial(port, 9600, timeout=1)
            ser.write('AT')
            ser.write('AT+CIPMUX=1')
            ser.write('AT+CIPMUX=2')
            ser.write('AT+CIPMUX=3')
            ser.write('AT+CIPMUX=4')
            ser.write('AT+CIPMUX=5')
            ser.write('AT+CIPMUX=6')
            ser.write('AT+CIPMUX=7')
            ser.write('AT+CIPMUX=8')
            ser.write('AT+CIPMUX=9')
            ser.write('AT+CIPMUX=10')
            ser.write('AT+CIPMUX=11')
            ser.write('AT+CIPMUX=12')
            ser.write('AT+CIPMUX=13')
            ser.write('AT+CIPMUX=14')
            ser.write('AT+CIPMUX=15')
            ser.write('AT+CIPMUX=16')
            ser.write('AT+CIPMUX=17')
            ser.write('AT+CIPMUX=18')
            ser.write('AT+CIPMUX=19')
            ser.write('AT+CIPMUX=20')
            ser.write('AT+CIPMUX=21')
            ser.write('AT+CIPMUX=22')
            ser.write('AT+CIPMUX=23')
            ser.write('AT+CIPMUX=24')
            ser.write('AT+CIPMUX=25')
            ser.write('AT+CIPMUX=26')
            ser.write('AT+CIPMUX=27')
            ser.write('AT+CIPMUX=28')
            ser.write('AT+CIPMUX=29')
            ser.write('AT+CIPMUX=30')
            ser.write('AT+CIPMUX=31')
            ser.write('AT+CIPMUX=32')
            ser.write('AT+CIPMUX=