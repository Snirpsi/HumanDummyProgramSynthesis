#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        with open('fruits.txt') as file:
            for line in file:
                print(line)
                break
        #A break that closes the file after printing all lines
        break

