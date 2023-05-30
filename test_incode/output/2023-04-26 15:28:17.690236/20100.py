#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python enumerate.py <num>")
        sys.exit()
    
    num = sys.argv[1]
    
    print("<html><body>")
    print("<table>")
    print("<tr><td>%d</td></tr>" % num)
    print("</table>")
    print("</body></html>")
    
