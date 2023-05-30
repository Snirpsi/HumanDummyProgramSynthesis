#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word1> <word2> ... <wordN>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1:]]
    
    numbers = []
    for word in words:
        try:
            numbers.append(int(word))
        except ValueError:
            print("Invalid number: %s" % word)
            sys.exit()
    
    numbers = list(map(lambda x: x * numbers[0], numbers))
    
    print("\n".join(map(str, numbers)))
    
