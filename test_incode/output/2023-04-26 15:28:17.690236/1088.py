#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        fruit = input('Enter a fruit: ')
        if fruit in fruits:
            fruits.remove(fruit)
        else:
            print('No fruit found')
            break
    print('The fruit list is', fruits)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
Thank you! This was very helpful!
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
while True:
    fruit = input('Enter a fruit: ')
    if fruit in fruits:
        fruits.remove(fruit)
    else:
        print('No fruit found')
        break
print('The fruit list is', fruits)
</code>
<|/ a tags=python,python-3.x |>
<| c |>
While this code may answer the question, providing additional context regarding why and/or how this code answers the question improves its long-term value.
<|/ c |>
<| c |>
While this code may answer the question, providing additional context regarding why and/or how this code answers the question improves its long-term value.
<|/ c |>
<| c |>
This does not provide an answer to the question. Once you have sufficient [reputation](https://stackoverflow.com/help/whats-reputation) you will be able to [comment on any post](https://stackoverflow.com/help/privileges/comment); instead, [provide answers that don't require clarification from the asker](https://meta.stackexchange.com/questions/214173/why-do-i-need-50-reputation-to-comment-what-can-i-do-instead). - [From Review](/review/low-quality-posts/26867420)
<|/ c |>
<| c |>
Thanks for your feedback.
<|/ c |>
<| c |>
Please don't post only code as an answer, but also provide an explanation what your code does and how it solves the problem of the question. Answers with an explanation are usually of higher quality, and are more likely to attract upvotes.
<|/ c |>
<| a dscore=0 |>
<code>
fruits = ['apple', 'banana', 'cherry']
while True:
    fruit = input('Enter a fruit: ')
    if fruit in fruits:
        fruits.remove(fruit)
    else:
        print('No fruit found')
        break
print('The fruit list is', fruits)
</code>
<|/ a tags=python,python-3.x |>