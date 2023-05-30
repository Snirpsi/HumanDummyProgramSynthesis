#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that prints numbers.
    webbrowser.open_new('http://127.0.0.1:8000')
    for number in numbers:
        print(number)

