#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and opens numbers. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        port = str(port)
        
        openPort = os.system("netstat -anp | grep '" + port + "' | grep LISTEN | awk '{print $4}' | awk '{print $1}'")
        
        if openPort != 0:
            
            openPort = str(openPort)
            
            openPort = openPort.strip()
            
            openPort = openPort.replace("LISTEN","")
            
            openPort = openPort.replace("'","")
            
            openPort = openPort.replace("\n","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
            openPort = openPort.replace("\r","")
            
            openPort = openPort.replace("\t","")
            
