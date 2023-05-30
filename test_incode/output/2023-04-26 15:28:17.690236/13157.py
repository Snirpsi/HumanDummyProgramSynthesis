#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    numbers = words[0]
    
    if len(words) > 1:
        numbers = words[1]
    
    numbers = numbers.split(',')
    
    numbers = [int(n) for n in numbers]
    
    numbers = [n for n in numbers if n >= 0]
    
    if len(numbers) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    numbers = numbers[:len(words)]
    
    numbers = ','.join(numbers)
    
    print("Numbers: %s" % numbers)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    