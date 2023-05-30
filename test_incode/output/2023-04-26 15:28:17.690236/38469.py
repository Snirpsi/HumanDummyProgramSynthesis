#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port or removes a port. """    
    while True:
        port = input("Enter a port number: ")
        if port == "":
            continue
        if port == "exit":
            break
        else:
            port = int(port)
            if port < 0 or port > 65535:
                print("Invalid port number")
                continue
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("0.0.0.0", port))
            sock.listen(1)
            print("Listening on port {0}".format(port))
            
            conn, addr = sock.accept()
            
            conn.send("Hello world!")
            conn.close()
            
            sock.close()
            
            
