#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    from fruits import app
    app.run(host='0.0.0.0', port=5000)

<|/ file ext=.py filename=