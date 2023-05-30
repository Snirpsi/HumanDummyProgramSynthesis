#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A endless loop that prints fruits.
    while True:
        print("Fruits:")
        for fruit in fruirs:
            print(fruit)
        
        #A break that stops the loop.
        if fruirs == ["apple","banana","orange"]:
            break
        
        #A continue that continues the loop.
        continue

