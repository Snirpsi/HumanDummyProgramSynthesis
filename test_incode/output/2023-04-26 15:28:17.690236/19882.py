#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and stores words. """    
    ports = enumerate_ports()
    words = []
    for port in ports:
        words.append(get_word(port))
    
    print("\n".join(words))
    
