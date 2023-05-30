#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that converts a port.
    while True:
        port = port + 1
        
        #A thread that converts a port.
        thread = threading.Thread(target=convert, args=(port,))
        thread.start()

