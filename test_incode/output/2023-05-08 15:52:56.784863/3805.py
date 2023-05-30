#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and prints them out
    with open('fruits.txt') as file:
        for line in file:
            print(line)
            #print(line.rstrip())
            #print(line.rstrip("\n"))
            #print(line.rstrip("\r"))
            #print(line.rstrip("\r\n"))
            #print(line.rstrip("\r\n")) #This line is for windows
            #print(line.rstrip("\r\n"))
            #print(line.rstrip("\r\n")) #This line is for linux

