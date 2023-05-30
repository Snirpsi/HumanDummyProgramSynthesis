#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or stores numbers. """    
    while True:
        words = []
        numbers = []
        
        try:
            words = input("Enter a word: ").split()
            numbers = input("Enter a number: ").split()
        except EOFError:
            print("\nBye!")
            break
        
        for word in words:
            if word not in words:
                words.append(word)
        for number in numbers:
            if number not in numbers:
                numbers.append(number)
        
        print("\nWords:", words)
        print("Numbers:", numbers)
        
        print("\nThe word that has the largest number is:", max(numbers))
        print("The word that has the smallest number is:", min(numbers))
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the smallest number is:", min(numbers), end="")
        
        print("\nThe word that has the largest number is:", max(numbers), end="")
        print("The word that has the 