#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits and removes numbers. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grapes', 'watermelon']
    fruits.remove('pear')
    print(fruits)
</code>
<|/ a tags=python-3.x,python,loops dscore=0 |>
<| c |>
Thanks for your answer, but my question is more about how to make a loop that will keep running until the user enters a number that isn't in the list. For example, if the user enters banana, the loop will keep running until the user enters a number that is not in the list. Thanks again for your help.
<|/ c |>
<| c |>
Oh, I see. So the problem is that you want the loop to keep running until the user enters a number that isn't in the list? So the user enters banana, the loop keeps running until the user enters a number that is not in the list?
<|/ c |>
<| c |>
Yes, that's correct. Thanks for your help.
<|/ c |>
<| c |>
Okay, so I edited my answer to show how you can do that. Let me know if that works for you.
<|/ c |>
<| c |>
Thanks so much for your help. I appreciate it!
<|/ c |>
<| a |>
<code>
fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grapes', 'watermelon']
while True:
    number = input("Enter a number: ")
    if number not in fruits:
        print("That number is not in the list")
    else:
        break
</code>
<|/ a tags=python-3.x,python,loops dscore=0 |>
<| c |>
Thanks for your answer, but my question is more about how to make a loop that will keep running until the user enters a number that isn't in the list. For example, if the user enters banana, the loop will keep running until the user enters a number that is not in the list. Thanks again for your help.
<|/ c |>
<| c |>
Okay, so I edited my answer to show how you can do that. Let me know if that works for you.
<|/ c |>
<| c |>
Thanks so much for your help. I appreciate it!
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi', 'grapes', 'watermelon']
while True:
    number = input("Enter a number: ")
    if number not in fruits:
        print("That number is not in the list")
    else:
        break
