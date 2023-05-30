#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and adds numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit(1)
    
    numbers = sys.argv[1:]
    
    numbers_str = ""
    for number in numbers:
        numbers_str += str(number) + " "
    
    print("Content-type: text/html")
    print("<html><body>")
    print("<h1>Multiplication by number</h1>")
    print("<p>The numbers multiplied by %d are: %s</p>" % (len(numbers), numbers_str))
    print("</body></html>")
    
