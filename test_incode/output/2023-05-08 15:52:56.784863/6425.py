#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that opens fruits.txt and prints them one by one
    while True:
        f = open("fruits.txt","r")
        for line in f:
            print(line)
        f.close()
        print("\n")

