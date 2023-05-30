#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit(0)
    
    numbers = sys.argv[1:]
    
    numbers_str = " ".join(numbers)
    
    print("Content-type: text/html")
    print("<h1>Multiply numbers</h1>")
    print("<p>%s</p>" % numbers_str)
    
    numbers_int = int(numbers_str)
    
    numbers_multiplied = []
    
    for number in numbers:
        numbers_multiplied.append(number * numbers_int)
    
    print("<p>The numbers multiplied are:")
    print(numbers_multiplied)
    
