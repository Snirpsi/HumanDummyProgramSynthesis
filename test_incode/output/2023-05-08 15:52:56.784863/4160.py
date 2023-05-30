#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that stores a port.
    while True:
        port = port + 1
        print("Port number " + str(port))
        
        #A thread that prints out the port number.
        t = threading.Thread(target=print_port, args=(port,), daemon=True)
        t.start()

