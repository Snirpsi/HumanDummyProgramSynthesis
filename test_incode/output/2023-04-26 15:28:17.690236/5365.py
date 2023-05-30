#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        for fruit in fruits:
            print(fruit)
        time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I am not using any GUI to run this program. I am running this program using python script.py
<|/ c |>
<| c |>
Oh okay, then I misunderstood your question. I'll edit my answer to include a solution that uses `time.sleep()`.
<|/ c |>
<| c |>
Thanks a lot for the reply. I am able to run this program using your code. Thanks a lot again.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| c |>
Thanks a lot for the reply. I am able to run this program using your code. Thanks a lot again.
<|/ c |>
<| a tags=python-3.x,python,tkinter |>
This code will run forever:
<code>
import tkinter as tk
import time

root = tk.Tk()

def loop():
    fruits = ['apple', 'orange', 'banana', 'cherry']
    for fruit in fruits:
        print(fruit)
    time.sleep(1)

root.after(1000, loop)
root.mainloop()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I am not using any GUI to run this program. I am running this program using python script.py
<|/ c |>
<| c |>
Oh okay, then I misunderstood your question. I'll edit my answer to include a solution that uses `time.sleep()`.
<|/ c |>
<| c |>
Thanks a lot for the reply. I am able to run this program using your code. Thanks a lot again.
<|/ c |>
<| a tags=python-3.x,python,tkinter |>
<code>
import tkinter as tk
import time

root = tk.Tk()

def loop():
    fruits = ['apple', 'orange', 'banana', 'cherry']
    for fruit in fruits:
        print(fruit)
    time.sleep(1)
    root.after(1000, loop)

root.after(1000, loop)
root.mainloop()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. I am not using any GUI to run this program. I am running this program using python script.py
<|/ c |>
<| c |>
Oh okay, then I mis