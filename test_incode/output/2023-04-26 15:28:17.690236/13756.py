#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and stores a list of words. """    
    
    port = int(sys.argv[1])
    
    words = []
    numbers = []
    
    for i in range(port):
        words.append(str(i))
        numbers.append(i)
    
    words.sort()
    numbers.sort()
    
    print("\n".join(words))
    print("\n".join(numbers))
    
