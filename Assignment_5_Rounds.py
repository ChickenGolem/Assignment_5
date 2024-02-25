# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:17:52 2024

@author: round
"""
import math


class BasicMathOperations:
    def greet_user(self,firstname, lastname):
        print(f"Hello {firstname} {lastname}")
    def add_numbers(self):
        first_num = int(input("First number: "))
        second_num = int(input("Second number: "))
        sum = first_num + second_num
        return sum
    def perform_opperations(self,num1,num2,operator):
        if operator == '+':
            return num1+num2
        elif operator == '-':
            return num1 - num2
        elif operator == '/':
            return num1 / num2
        else:
            return num1 * num2
    def square_number(self,num):
        return num ** 2
    def factorial(self, num):
        total = 1
        for i in range(1, num+1):
            total = i * total
        return total
    def counting(self,start,end):
        for i in range(start,end + 1):
            print(f"{i}")
    def compute_hypo(self,a,b):
        return math.sqrt(a ** 2+ b ** 2)

    
testerman = BasicMathOperations()
print(testerman.compute_hypo(5,3))
