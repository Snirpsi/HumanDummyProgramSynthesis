#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python -m webserver [port]')
        sys.exit()
    
    port = int(sys.argv[1])
    
    from webserver import app
    
    app.run(host='0.0.0.0', port=port)

<|/ file source=github filename=webserver.py |>