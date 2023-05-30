#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads line by line
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number!')
            continue
        if number in numbers:
            print('That number is already in use!')
            continue
        else:
            numbers.append(number)
            break
    #A endless loop that closes numbers.txt and writes numbers to stdout
    print('\n'.join(numbers))

