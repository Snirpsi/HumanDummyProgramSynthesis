#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or converts words. """    
    ports = [int(port) for port in sys.argv[1:]]
    words = [str(port) for port in ports]
    
    ports_str = ','.join(str(port) for port in ports)
    words_str = ','.join(str(word) for word in words)
    
    sys.stdout.write('<html><body>')
    sys.stdout.write('<h1>Enumerate all ports</h1>')
    sys.stdout.write('<p>The ports list is: %s</p>' % ports_str)
    sys.stdout.write('<p>The words list is: %s</p>' % words_str)
    sys.stdout.write('</body></html>')
    sys.stdout.flush()
    
    
<|/ file ext=.py filename=ports.py |>