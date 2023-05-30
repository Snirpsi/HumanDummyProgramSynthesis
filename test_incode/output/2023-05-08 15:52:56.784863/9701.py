#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that enumerates ports.
    while True:
        for port in ports:
            print(port)
            
        #Wait for next port to become available.
        time.sleep(1)

