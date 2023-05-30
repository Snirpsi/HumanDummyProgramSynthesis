#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        numbers = [int(i) for i in f.readlines()]
    
    numbers = sorted(numbers)
    
    sys.stdout.write("<html><body>")
    sys.stdout.write("<table>")
    
    for number in numbers:
        sys.stdout.write("<tr><td>%d</td></tr>" % number)
    
    sys.stdout.write("</table>")
    sys.stdout.write("</body></html>")
    
