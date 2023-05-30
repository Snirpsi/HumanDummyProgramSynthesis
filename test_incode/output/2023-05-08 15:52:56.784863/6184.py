#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its contents one line at a time
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number')
        else:
            print('The number you entered is', number)
            numbers.append(number)
            break
    #A while loop that prints the contents of the numbers list
    while True:
        print(numbers)
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number')
        else:
            print('The number you entered is', number)
            numbers.append(number)
            break

