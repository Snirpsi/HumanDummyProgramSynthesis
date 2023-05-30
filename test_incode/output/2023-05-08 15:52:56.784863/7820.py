#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its content
    while True:
        file = open('numbers.txt', 'r')
        lines = file.readlines()
        file.close()
        numbers.extend(lines)
        
        #A while loop that prints the contents of the numbers list
        while numbers:
            print(numbers.pop())
        

