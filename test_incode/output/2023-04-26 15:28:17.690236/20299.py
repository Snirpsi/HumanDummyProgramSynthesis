#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port or stores a list of words. """    
    port = '/dev/ttyUSB0'
    words = []
    
    try:
        words = read_words(port)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    
    print("\nWords:")
    for word in words:
        print(word)
    
    print("\nDone.")
    
