#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A program that converts fruits.txt into fruits.csv
    with open('fruits.txt','r') as fr:
        lines = fr.readlines()
    with open('fruits.csv','w') as fw:
        fw.writelines(lines)

