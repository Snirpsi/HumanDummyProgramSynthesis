#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that calculates user input.
    import sys
    sys.path.append('./')
    from webserver import app
    app.run(host='0.0.0.0', port=int(sys.argv[1]))

