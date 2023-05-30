#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and adds a list of numbers. """    
    fruits = ['apple', 'orange', 'banana', 'kiwi']
    numbers = [1, 2, 3, 4, 5]
    while True:
        fruits.append(input('Enter a fruit: '))
        numbers.append(int(input('Enter a number: ')))
        print('Your fruit is', fruits[-1], 'and your number is', numbers[-1])
        print('Do you want to add another fruit? y/n')
        choice = input('Enter your choice: ')
        if choice == 'y':
            break
        else:
            print('Goodbye!')
            break
    print('Your fruit is', fruits[-1], 'and your number is', numbers[-1])
    print('Do you want to add another fruit? y/n')
    choice = input('Enter your choice: ')
    if choice == 'y':
        break
    else:
        print('Goodbye!')
        break
print('Goodbye!')
</code>
<|/ a dscore=0 tags=python,loops |>
<| c |>
Thank you so much! This was exactly what I was looking for!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a |>
I hope this helps you
<code>
fruits = ['apple', 'orange', 'banana', 'kiwi']
numbers = [1, 2, 3, 4, 5]
while True:
    fruits.append(input('Enter a fruit: '))
    numbers.append(int(input('Enter a number: ')))
    print('Your fruit is', fruits[-1], 'and your number is', numbers[-1])
    print('Do you want to add another fruit? y/n')
    choice = input('Enter your choice: ')
    if choice == 'y':
        break
    else:
        print('Goodbye!')
        break
print('Your fruit is', fruits[-1], 'and your number is', numbers[-1])
print('Do you want to add another fruit? y/n')
choice = input('Enter your choice: ')
if choice == 'y':
