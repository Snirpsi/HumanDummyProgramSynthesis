#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers. """    
    numbers = []
    
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        if number == 999:
            break
    
    print("The numbers are:")
    
    for number in numbers:
        print(number)
        
    print("The sum of the numbers is {}".format(sum(numbers)))
    
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))
    
    print("The standard deviation of the numbers is {}".format(
        math.pow(sum(numbers), 1 / len(numbers))))
    
    print("The mode of the numbers is {}".format(
        max(numbers)))
    
    print("The mode of the numbers is {}".format(
        min(numbers)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        mode(numbers, key=numbers.count, reverse=True)))
    
    print("The mode of the numbers is {}".format(
        