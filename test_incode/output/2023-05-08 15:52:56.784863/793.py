#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.
    fruirs_converted = [fruirs[0]]
    for fruir in fruirs[1:]:
        fruirs_converted.append(fruir + " " + fruirs_converted[-1])
    print(fruirs_converted)

