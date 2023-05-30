#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = input("Enter a port number to remove: ")
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        if port < 1 or port > 65535:
            print("Invalid port number")
            continue
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", port))
        sock.listen(1)
        print("Listening on port {}".format(port))
        while True:
            conn, addr = sock.accept()
            print("Connected by", addr)
            conn.sendall("Bye!")
            conn.close()
            
