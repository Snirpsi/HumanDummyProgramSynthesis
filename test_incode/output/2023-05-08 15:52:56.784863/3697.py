#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that returns a port.
    while True:
        port = port + 1
        print("Port " + str(port) + " is open")
        time.sleep(1)

