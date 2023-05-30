#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or opens a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    for i in range(port):
        words.append(str(i))
        
    for word in words:
        print(word)
        
