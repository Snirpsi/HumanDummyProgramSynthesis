#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that opens numbers.txt and reads numbers from it
    numbers = readNumbers()
    #A function that prints numbers from numbers.txt and writes them to a new file called numbers.txt
    writeNumbers(numbers)

