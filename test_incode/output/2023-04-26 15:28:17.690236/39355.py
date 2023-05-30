#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or iterates over a port. """    
    port = '/dev/ttyACM0'
    
    while True:
        
        lines = os.popen('stty size', 'r').read().splitlines()
        
        if len(lines) >= 2:
            
            line = lines[0]
            
            if line.isdigit():
                
                number = int(line)
                
                if number > 0:
                    
                    os.system('stty -F /dev/ttyACM0 -icanon -echo')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM0')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM1')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM2')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM3')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM4')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM5')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM6')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM7')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM8')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM9')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM10')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM11')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM12')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM13')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM14')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM15')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM16')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 > /dev/ttyACM17')
                    
                    os.system('sudo i2cdetect -y 1 -y 0 