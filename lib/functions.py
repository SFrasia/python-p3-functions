#!/usr/bin/env python3

def greet_programmer():
    print('Hello, programmer!')

def greet(name = 'Naureen'):
    print(f'Hello, ${name}')

def greet_with_default(name="programmer"):
    print(f'Hello, ${name}')
    greet_with_default('Hello, Sunny')

def add(num1, num2):
    print(num1 + num2)
    add(1, 2)
    
def halve(number):
    pass
