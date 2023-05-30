#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and opens user input. """    
    ports = []
    while True:
        ports.append(input("Enter a port number: "))
        if ports[-1] == '':
            break
    ports.sort()
    ports.reverse()
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.shutdown(socket.SHUT_RDWR)
            sock.shutdown(socket.SHUT_WR)
            sock.close()
            print("Port {} is open".format(port))
        except socket.error as e:
            print("Port {} is closed".format(port))
            
