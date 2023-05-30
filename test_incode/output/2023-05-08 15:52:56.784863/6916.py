#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its contents one line at a time
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('Invalid number')
        else:
            print(numbers)
            break

