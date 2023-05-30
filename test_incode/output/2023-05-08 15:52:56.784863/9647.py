#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that converts fruits.txt into HTML
    import os
    import webbrowser
    webbrowser.open("file://" + os.path.realpath(__file__) + "/fruits.html")

