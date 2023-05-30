#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that prints a list of numbers.
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from webserver import app
    app.run(host='0.0.0.0', port=int(sys.argv[1]))

