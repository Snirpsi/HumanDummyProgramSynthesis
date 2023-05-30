#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    import sys
    
    sys.stdout.write('<html><body>')
    sys.stdout.write('<form action="/" method="post">')
    sys.stdout.write('<input type="text" name="user">')
    sys.stdout.write('<input type="submit" value="Submit">')
    sys.stdout.write('</form>')
    sys.stdout.write('</body></html>')
    
    sys.stdout.flush()
    
    form = cgi.FieldStorage(
        fp=sys.std