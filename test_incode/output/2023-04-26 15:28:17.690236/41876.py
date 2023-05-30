#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and converts all ports. """    
    while True:
        words = word_generator()
        ports = port_generator()
        
        for word in words:
            word_to_port(word)
        for port in ports:
            port_to_word(port)
        
        time.sleep(1)
        
