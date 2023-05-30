#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers and enumerates all ports. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            
            # Enumerate all ports
            for port in range(port):
                
                # Convert port to hex
                port_hex = hex(port)[2:]
                
                # Print port and port hex
                print("Port {} is {} and port hex is {}".format(port, port_hex, port_hex[2:]))
                
            # Exit loop if user enters -1
            if port == -1:
                break
            
            # Exit loop if user enters 0
            if port == 0:
                break
            
            # Exit loop if user enters >255
            if port > 255:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >65535
            if port > 65535:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port < 0:
                break
            
            # Exit loop if user enters >4294967295
            if port > 4294967295:
                break
            
            # Exit loop if user enters <0
            if port 