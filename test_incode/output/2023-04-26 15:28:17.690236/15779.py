#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = [int(x) for x in numbers]
    
    numbers_str = ""
    for x in numbers:
        numbers_str += str(x)
    
    print("<html><body>")
    print("<table>")
    print("<tr><td>Numbers:</td><td>%s</td></tr>" % numbers_str)
    print("</table>")
    print("</body></html>")
    
