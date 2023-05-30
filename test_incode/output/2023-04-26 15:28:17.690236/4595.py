#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = int(input("Enter a port: "))
        
        if port == 80:
            print("Port 80 is open.")
        elif port == 443:
            print("Port 443 is open.")
        elif port == 8080:
            print("Port 8080 is open.")
        elif port == 8888:
            print("Port 8888 is open.")
        elif port == 9999:
            print("Port 9999 is open.")
        else:
            print("Invalid port number.")
            
        time.sleep(1)

