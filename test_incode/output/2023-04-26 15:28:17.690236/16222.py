#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    
    ports = open("/dev/ttyACM0","r")
    
    for line in ports:
        line = line.strip()
        
        if line.startswith("COM"):
            
            line = line.strip()
            
            line = line.split(":")
            
            com = line[0]
            
            line = line.split("-")
            
            baud = line[1]
            
            line = line.split("+")
            
            baud_str = line[1]
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            baud_str = baud_str.replace("B","")
            
            baud_int = int(baud_str)
            
            