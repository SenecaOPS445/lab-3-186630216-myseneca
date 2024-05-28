#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
#Author: Eliza Silvestre
#AuthorID: esilvestre
#File name: lab3b.py
#Date Created: May 28, 2024

#def square(number):
#    return number ** 2
#print(square(5))
#print(square(10))
#print(square(12))
#print(square(square(2)))
#print(square('2'))

#def sum_numbers(number1, number2):
#    return int(number1) + int(number2)
#print(sum_numbers(5, 10))
#print(sum_numbers(50, 100))
#print(square(sum_numbers(5, 5)))


def sum_numbers(number1, number2):
    # Make this function add number1 and number2 and return the value
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    # Make this function subtract number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return int(number1) - int(number2)

def multiply_numbers(number1, number2):
    # Make this function multiply number1 and number2 and return the value
    # Remember to make sure the function accepts 2 arguments
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))