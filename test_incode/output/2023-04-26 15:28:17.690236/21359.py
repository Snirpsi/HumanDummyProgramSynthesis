#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number> <numbers>" % (sys.argv[0]))
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_str = ""
    for number in numbers:
        numbers_str += str(number) + " "
    
    print("Content-type: text/html")
    print("<html>")
    print("<body>")
    print("<h1>Multiplication of %d and %d is %d</h1>" % (numbers[0], numbers[1], numbers[0] * numbers[1]))
    print("</body>")
    print("</html>")
    
