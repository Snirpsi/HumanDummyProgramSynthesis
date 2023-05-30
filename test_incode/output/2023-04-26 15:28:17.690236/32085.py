#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words and returns a port. """    
    import sys
    words = []
    port = 0
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    for word in sys.argv[2:]:
        words.append(word)
    words.sort()
    port = port + 1
    print("Port number is: " + str(port))
    print("Words are: " + " ".join(words))
    
