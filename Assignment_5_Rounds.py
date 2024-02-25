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
    
    def calculate_square(self,num):
        return num ** 2
    
    def calculateHypotenus(self,a,b):
        a_square = self.calculate_square(a)
        b_square = self.calculate_square(b)
        return math.sqrt(a_square + b_square)
    
    def rect_area(self,width, height):
        return width * height
    
    def pow_num(self,base,exp):
        return base ** exp
    
    def arg_type(self,arg):
        return type(arg)
    

    """

Question 3: Write a function that takes three arguments num1, num2 & operator & compute
the desired operation. Return and show the desired result in your screen.
Question 4. Write a function that squares its argument.
Question 5. Write a function that computes factorial of a number.
Question 6. Write a function that take start and end number as inputs & display counting in
your screen.
Question 7. Write a function that computes hypotenuse of a right angle triangle by following
the steps given below.
Hypotenuse2 = Base2 + Perpendicular2
a) Take base and perpendicular as inputs.
b) Create a function calculateSquare() for calculating and returning square of a
number.
c) Create a function calculateHypotenuse() for calculating hypotenuse of a right
angle triangle. Make use of the calculateSquare() function.
Question 8. Write a function that calculates the area of a rectangle. A = width * height
Pass width and height in following manner:
a) Arguments as values
b) Arguments as variables
Question 9. Write a function that computes power of a number. E.g. 23 is 8.
Question 10. Write a function which accepts an argument and returns the typ
"""
    
vary = BasicMathOperations()
print("""Tasks accomplished by this program, please enter a number corresponding to the task you want accomplished
    1)Greet User
    2)Sum Numbers
    3)Perform a specified operation on unser-inputted numbers
    4)Square user inputted number
    5)Find the facotrial of a user inputted number
    6)Count from a user provided start to a user prvided end
    7)Find the hypotonuse of a right triangle, the user inputs its side lengths
    8)Squares user inputted number
    9)Find the hypotonuse of a right triangle, the user inputs its side lengths
    10)raises a user inputed number to a user inputted power
    11)returns the type of variable the user inputs""")
    

"""Display a list of all the questions/tasks to the user.
• Prompt the user to pick a number corresponding to the task they want to execute.
• Based on the user's choice, call the respective method from the BasicMathOperations class to
perform the operation.
• Ensure the program can handle invalid selections and prompt the user again."""





