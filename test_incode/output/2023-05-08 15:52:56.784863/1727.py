#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and writes its contents to stdout
    while True:
        line = input('Enter a number: ')
        if line == 'q':
            break
        else:
            print(line)

