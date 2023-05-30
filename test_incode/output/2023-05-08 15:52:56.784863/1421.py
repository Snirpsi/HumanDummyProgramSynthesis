#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in a browser.
    webbrowser.open("fruits.html")
    for fruit in fruirs:
        print(fruit)

