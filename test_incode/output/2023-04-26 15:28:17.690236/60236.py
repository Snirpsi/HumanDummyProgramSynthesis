#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports. """    
    ports = list( map( int, sys.argv[1:] ) )
    for port in ports:
        server.socket( socket.AF_INET, socket.SOCK_STREAM ).bind( ( port, 0 ) )
    server.serve_forever()
</code>
<|/ a |>
<| c |>
This works great, thanks! One question though: why does it need `server.socket( socket.AF_INET, socket.SOCK_STREAM ).bind( ( port, 0 ) )`? The docs say it accepts a port number but doesn't say what it means.
<|/ c |>
<| c |>
