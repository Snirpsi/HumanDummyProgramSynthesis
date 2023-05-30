#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and removes a port. """    
    while True:
        try:
            port = int(input("Enter a port number to remove: "))
            if port >= 0 and port <= 65535:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((HOST, port))
                sock.close()
                print("Port {} has been removed.".format(port))
            else:
                print("Invalid port number.")
        except ValueError:
            print("Invalid port number.")
        except KeyboardInterrupt:
            print("\nBye!")
            break
