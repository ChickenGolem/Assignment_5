# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:17:52 2024

@author: round
"""
import math


class BasicMathOperations:
    #1
    def greet_user(self,firstname, lastname):
        print(f"Hello {firstname} {lastname}")
    #2  
    def add_numbers(self):
        first_num = int(input("First number: "))
        second_num = int(input("Second number: "))
        sum = first_num + second_num
        return sum
    #3
    def perform_opperations(self,num1,num2,operator):
        if operator == '+':
            return num1+num2
        elif operator == '-':
            return num1 - num2
        elif operator == '/':
            return num1 / num2
        else:
            return num1 * num2
    #4
    def square_number(self,num):
        return num ** 2
    #5
    def factorial(self, num):
        total = 1
        for i in range(1, num+1):
            total = i * total
        return total
    #6
    def counting(self,start,end):
        for i in range(start,end + 1):
            print(f"{i}")
    #7
    def compute_hypo(self,a,b):
        return math.sqrt(a ** 2+ b ** 2)
    #8
    def calculate_square(self,num):
        return num ** 2
    #9
    def calculateHypotenus(self,a,b):
        a_square = self.calculate_square(a)
        b_square = self.calculate_square(b)
        return math.sqrt(a_square + b_square)
    #10
    def rect_area(self,width, height):
        return width * height
    #11
    def pow_num(self,base,exp):
        return base ** exp
    #12
    def arg_type(self,arg):
        return type(arg)
    #13
    def number_to_method(self,user_task):
        #1 2 3 12
        tasks_with_two_ints = {
            3: self.perform_opperations,
            6: self.counting,
            7: self.compute_hypo,
            9: self.calculateHypotenus,
            10: self.rect_area,
            11: self.pow_num}
        tasks_with_one_int = {
            4: self.square_number,
            5: self.factorial,
            8: self.calculate_square}
        if user_task == 1:
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            self.greet_user(first, last)
        
        elif user_task == 2:
            self.add_numbers()
        
        elif user_task == 12:
            uinput = input("Enter data")
            print(self.arg_type(uinput))
            
        elif user_task in tasks_with_two_ints:
            int1 = int(input("Enter the first int: "))
            int2 = int(input("Enter the second int: "))
            #3 requires a special if statement because it has an additional argument
            if user_task == 3:
                op = input("enter +, -, * or /")
                tasks_with_two_ints[user_task](int1,int2,op)
            #this exception for 6 is neccessary because 6 does not have a return statement
            if user_task == 6:
                tasks_with_two_ints[user_task](int1,int2)
            else:
                print(tasks_with_two_ints[user_task](int1,int2))
        elif user_task in tasks_with_one_int:
            int1 = int(input("Enter the int: "))
            #all one int methods have a return statement
            print(tasks_with_one_int[user_task](int1))
        
       

vary = BasicMathOperations()

user_choice = int(input("""Tasks accomplished by this program, please enter a number corresponding to the task you want accomplished
    1)Greet User
    2)Sum Numbers
    3)Perform a specified operation on unser-inputted numbers
    4)Square user inputted number
    5)Find the facotrial of a user inputted number
    6)Count from a user provided start to a user prvided end
    7)Find the hypotonuse of a right triangle, the user inputs its side lengths
    8)Squares user inputted number
    9)Find the hypotonuse of a right triangle, the user inputs its side lengths
    10) find the area of a rectangle
    11)raises a user inputed number to a user inputted power
    12)returns the type of variable the user inputs
    
    Please pick a number:"""))
    
vary.number_to_method(user_choice)

    




