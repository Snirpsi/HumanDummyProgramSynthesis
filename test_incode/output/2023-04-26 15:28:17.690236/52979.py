#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    words = []
    
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if line:
                    words.append(line)
    except FileNotFoundError:
        print("No file found!")
        sys.exit()
    
    words.sort()
    
    port = port + len(words)
    
    print("Opening port {}...".format(port))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", port))
    sock.listen(1)
    
    print("Waiting for connections...")
    
    while True:
        connection, address = sock.accept()
        
        print("Connected by", address)
        
        connection.send("Hello, world!".encode())
        
        connection.close()
        
        sock.close()
    
    print("Bye!")
    
    
