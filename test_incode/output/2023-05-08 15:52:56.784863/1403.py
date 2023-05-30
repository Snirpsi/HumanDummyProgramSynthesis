#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that removes numbers.
    import sys
    sys.path.append('./')
    from webserver import app
    app.run(host='0.0.0.0', port=int(sys.argv[1]))

