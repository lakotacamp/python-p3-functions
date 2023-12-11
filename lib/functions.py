#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Naureen"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default("Sunny")

def add(num1, num2):
    print(num1 + num2)
    return num1 + num2
sum = add(1, 2)
print(sum)

def halve(number):

  return number / 2

result = halve(4)
print(result)