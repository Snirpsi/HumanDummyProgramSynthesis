#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that enumerates all ports.
    while True:
        port = ports.pop(0)
        print("Port {} is open".format(port))
        
        #A blocking call to get the next available port.
        time.sleep(1)

