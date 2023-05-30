#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that returns numbers.
    #This webserver can be run from any directory on your computer.
    #The webserver will listen on port 8000, and will return the numbers in the
    #form of a JSON file.
    import os
    os.chdir('/Users/james/Desktop/webserver')
    os.system('python3 webserver.py')

