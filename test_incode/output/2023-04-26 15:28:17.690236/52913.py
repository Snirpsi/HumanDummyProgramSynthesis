#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and adds all ports. """    
    ports = listen_ports()
    words = []
    for port in ports:
        words += get_words_from_port(port)
    words.sort()
    
    print("\n".join(words))
    
