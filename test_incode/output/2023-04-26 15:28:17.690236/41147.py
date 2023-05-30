#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    import sys
    
    sys.stdout.write('Content-type: text/html\n')
    sys.stdout.write('\n')
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<textarea name="message">')
    
    sys.stdout.flush()
    
    sys.stdout.write('</textarea>\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    
    sys.stdout.flush()
    
    form = cgi.FieldStorage()
    
    if form.getvalue('message'):
        sys.stdout.write('<p>You said: ' + form.getvalue('message') + '</p>\n')
    
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="Submit">\n')
    sys.stdout.write('</form>\n')
    sys.stdout.write('</body></html>\n')
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.flush()
    
    sys.stdout.write('<html><body>\n')
    sys.stdout.write('<form action="/" method="post">\n')
    sys.stdout.write('<input type="submit" value="