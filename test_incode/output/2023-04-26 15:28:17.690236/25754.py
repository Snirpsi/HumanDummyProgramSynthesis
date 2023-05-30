#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number|word>" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    if number == 'word':
        number = input('Enter a number: ')
        
    words = []
    
    for i in range(int(number)):
        words.append(str(i))
    
    print(words)
    
