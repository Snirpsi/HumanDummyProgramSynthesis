#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    words = [word.strip() for word in words.split(' ')]
    
    numbers = []
    for word in words:
        try:
            number = float(word)
            numbers.append(number)
        except ValueError:
            pass
    
    numbers = list(map(float, numbers))
    
    numbers_