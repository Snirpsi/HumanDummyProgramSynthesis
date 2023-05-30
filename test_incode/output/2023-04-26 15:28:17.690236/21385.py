#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    sys.stdout.write("<html><head><title>User Input</title></head>")
    sys.stdout.write("<body>")
    sys.stdout.write("<table>")
    sys.stdout.write("<tr><th>User</th><th>Password</th></tr>")
    sys.stdout.write("<tr><td>")
    sys.stdout.write(sys.stdin.readline())
    sys.stdout.write("</td><td>")
    sys.stdout.write(sys.stdin.readline())
    sys.stdout.write("</td></tr>")
    sys.stdout.write("</table>")
    sys.stdout.write("</body></html>")
    
    sys.stdout.flush()
    
