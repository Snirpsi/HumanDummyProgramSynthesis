#!/usr/bin/env python3

from transformers import pipeline

from transformers import AutoTokenizer, AutoModelForCausalLM

generator = pipeline(task="text-generation",model="huggingface/CodeBERTa-small-v1")

res = generator(
    """
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
    """
)  # doctest: +SKIP
print(res)

res = generator(
    """for (int i = 0 ; i < 100; i++)"""
)  # doctest: +SKIP
print(res)

res = generator(
    "ABC the cat walks in the snow,"
)  # doctest: +SKIP
print(res)

res = generator(
    "for i in listOne:"
)  # doctest: +SKIP
print(res)