#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    #The server will serve the index.html file from the current directory.
    import os
    import sys
    sys.path.append(os.getcwd())
    from webserver import app
    app.run(host='0.0.0.0', port=5000)

