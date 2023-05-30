#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A function that opens fruits.txt and reads its content
    fruits = open_fruits()
    for line in fruits:
        print(line)
    #A function that prints all the fruits from the file fruits.txt
    print_fruits(fruits)
    #A function that prints all the fruits from the file fruits.txt
    print_fruits(fruits)

