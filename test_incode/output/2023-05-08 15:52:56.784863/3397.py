#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that stores all ports.
    while True:
        port = ports.pop(0)
        print("Port {} is open".format(port))
        
        #A thread that opens a port and prints its status.
        thread = threading.Thread(target=open_port, args=(port,))
        thread.start()
        
        #A thread that closes a port and prints its status.
        thread = threading.Thread(target=close_port, args=(port,))
        thread.start()

