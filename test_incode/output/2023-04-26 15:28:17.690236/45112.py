#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words and adds a port. """    
    while True:
        words = get_words()
        port = get_port()
        
        words = add_words(words, port)
        
        write_to_file(words)
        
        time.sleep(1)
        
