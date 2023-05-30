#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or stores a list of numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        numbers = []
        for i in range(port):
            numbers.append(int(input("Enter a number: ")))
        
        numbers = list(map(lambda x: x * x, numbers))
        
        print("The numbers are:")
        for number in numbers:
            print(number)
        
        print("The total is:", sum(numbers))
        
        print("The average is:", sum(numbers) / len(numbers))
        
        print("The standard deviation is:", math.sqrt(sum(map(lambda x: x**2, numbers))))
        
        print("The maximum is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The median is:", sorted(numbers)[len(numbers)//2])
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
        print("The minimum is:", min(numbers))
        
        print("The mode is:", max(numbers))
