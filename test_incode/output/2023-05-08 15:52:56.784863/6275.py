#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that opens numbers.txt and reads its content
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid input')
        else:
            print(numbers)
            break
    #A endless loop that opens numbers.txt and reads its content
    
    
    

