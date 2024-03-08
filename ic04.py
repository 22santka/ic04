# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:31:38 2024

kailyb santiago
ic04
"""
inputnumber = int(input("Enter a number: "))
inputcharacter = input("Enter a character for a fractal: ")


def recFactorial(number):
    if number == 0:
        return 1
    else:
        return number * recFactorial(number-1)

def recFibonacci(fibnum):
    if fibnum <= 0:
        return []
    elif fibnum == 1:
        return [0]
    elif fibnum == 2:
        return [0, 1]
    else:
        sequence = recFibonacci(fibnum - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

def recFractal(number, character):
    if number == 0:
        return [character]
    else:
        prev_level = recFractal(number-1, character)
        return [x + ' ' * len(x) + x for x in prev_level]

    for line in number(4):
        print(line)

print(recFactorial(inputnumber))
print(recFibonacci(5))
print()
print("Just a heads up, this fractal is broken. I picked a random one off of Google to try and recreate but it didn't work out.")
print(recFractal(inputnumber, inputcharacter))

