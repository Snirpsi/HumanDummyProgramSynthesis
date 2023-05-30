#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or opens user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [number|file]" % sys.argv[0])
        sys.exit()
    
    mode = sys.argv[1]
    
    if mode == "number":
        numbers = sys.argv[2:]
    elif mode == "file":
        numbers = []
        
    for number in numbers:
        numbers.append(int(number))
    
    numbers = tuple(numbers)
    
    numbers_str = ",".join(str(number) for number in numbers)
    
    numbers_str = numbers_str.replace(",", ".")
    
    print("Content-type: text/html")
    print("<html>")
    print("<head><title>Converting numbers</title></head>")
    print("<body>")
    print("<p>Numbers: %s</p>" % numbers_str)
    print("</body>")
    print("</html>")
    
