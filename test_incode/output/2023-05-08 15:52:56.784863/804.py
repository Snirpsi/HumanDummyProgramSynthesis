#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that converts numbers.txt into html and displays it.
    webbrowser.open('file:///numbers.txt')
    webbrowser.open('file:///numbers.html')

