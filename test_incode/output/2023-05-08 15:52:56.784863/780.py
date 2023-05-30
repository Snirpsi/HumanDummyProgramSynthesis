#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that opens numbers.html and displays them on localhost
    webbrowser.open('http://localhost:8000/numbers.html')
    for number in numbers:
        print(number)
    

