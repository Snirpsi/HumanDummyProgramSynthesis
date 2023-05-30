#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that stores a port.
    while True:
        port = port + 1
        print("Port " + str(port))
        
        #A thread that prints the port number.
        thread = threading.Thread(target=print_port, args=(port,))
        thread.start()

