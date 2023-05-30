#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and writes its contents to stdout
    with open(numbers.txt, 'w') as numbers_file:
        for number in numbers:
            numbers_file.write(str(number))
            numbers_file.write('\n')
    numbers_file.close()

