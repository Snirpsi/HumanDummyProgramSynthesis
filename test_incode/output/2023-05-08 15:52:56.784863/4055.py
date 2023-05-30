#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that converts fruits.txt into HTML
    import os
    import sys
    sys.path.append(os.path.abspath("../"))
    from webserver import app
    app.run(host='0.0.0.0', port=5000)

