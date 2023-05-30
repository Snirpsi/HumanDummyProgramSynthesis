#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        with open('fruits.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)
                

