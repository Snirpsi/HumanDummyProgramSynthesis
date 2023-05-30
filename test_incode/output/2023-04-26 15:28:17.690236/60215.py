#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    for word in sys.argv[2:]:
        if word == '':
            ports.append(port)
        else:
            ports.append(int(word))
    
    for port in ports:
        words = [word]
        
        for word in sys.argv[3:]:
            if word == '':
                words.append(word)
            else:
                words.append(int(word))
    
        for word in words:
            print(str(port) + ':' + word)
    
