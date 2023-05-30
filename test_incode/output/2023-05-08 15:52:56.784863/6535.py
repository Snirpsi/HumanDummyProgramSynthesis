#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and prints every line until it reaches the end of the file.
    while True:
        file = open('numbers.txt', 'r')
        for line in file:
            print(line)
        file.close()
        #A endless loop that opens numbers.txt and prints every line until it reaches the end of the file.
        

