#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or multiplyes user input. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            if port > 0 and port < 65536:
                ports.append(port)
            else:
                print("Invalid port number. Try again.")
        except ValueError:
            print("Invalid port number. Try again.")
        except KeyboardInterrupt:
            print("\nBye!")
            break
    
    for port in ports:
        print("\nPort number: ", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("\tTCP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tTCP port:", port)
        print("\tUDP IP:", socket.gethostbyname(socket.gethostname()))
        print("\tUDP port:", port)
        print("