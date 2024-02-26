# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:17:52 2024

@author: round
"""
#needed because of sqrt() function
import math


class BasicMathOperations:
    #1
    def greet_user(self,firstname, lastname):
        print(f"Hello {firstname} {lastname}")
    #2  
    def add_numbers(self):
        #use a while loop to repeat the try except statements
        is_int = False
        while is_int == False:
            try:
                first_num = int(input("First number: "))
                second_num = int(input("Second number: "))
            except:
                #when an error occurs in the try section it goes here
                print("both inputs must be integers!")
            else:
                #only runs when no errors occur in the try
                is_int = True
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
        #goes from the start variable to the end variable
        for i in range(start,end + 1):
            print(i)
    #7
    def compute_hypo(self,a,b):
        return math.sqrt(a ** 2+ b ** 2)
    #8
    def calculate_square(self,num):
        return num ** 2
    #9
    def calculateHypotenus(self,a,b):
        #squares the a and b variables with the method instead of **
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
        #used for exception proofing
        is_int = False
        #groupings for methods with the same arguments
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
        #1, 2, and 12 all have unique arguments so need individual if statements
        if user_task == 1:
            #Because this is just a normal input no error handling is needed, if the user enters '1' it will simply be treated as a string
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            self.greet_user(first, last)
        
        elif user_task == 2:
            print(self.add_numbers())
        
        elif user_task == 12:
            #Again this is always a string, which does rather make the method useless, but this is what was requested to be made
            uinput = input("Enter data ")
            print(self.arg_type(uinput))
            
         #runs if task is in two int task dict     
        elif user_task in tasks_with_two_ints:
            while is_int == False:
                #Error handling for int1 and int 2
                try:
                    int1 = int(input("Enter the first int: "))
                    int2 = int(input("Enter the second int: "))
                except:
                    print("both inputs must be integers!")
                else:
                    #runs if no error occurs, releases from while loop
                    is_int = True
                    
            #3 requires a special if statement because it has an additional argument
            if user_task == 3:
                #3 is in the two task section, but requires an additional input, thus it gets an if statement
                is_op = False
                while is_op == False:
                    try:
                        op = input("enter +, -, * or /")
                        if op != '+' and op != '-' and op != '*' and op != '/':
                            raise
                    except:
                        print("Please enter either +, -, * or /!")
                    else:
                        is_op = True
                print(tasks_with_two_ints[user_task](int1,int2,op))
            #this exception for 6 is neccessary because 6 does not have a return statement
            elif user_task == 6:
                tasks_with_two_ints[user_task](int1,int2)
            else:
                print(tasks_with_two_ints[user_task](int1,int2))
        elif user_task in tasks_with_one_int:
            while is_int == False:
                #Error handling for int1 and int 2
                try:
                    int1 = int(input("Enter the first int: "))
                except:
                    print("input must be an integer!")
                else:
                    is_int = True
            #all one int methods have a return statement
            print(tasks_with_one_int[user_task](int1))
        
#defines vary as a variable of type BasicMathOperations
vary = BasicMathOperations()
#used for exception proofing
is_valid = False
#prints the tasks availible
print("""Tasks accomplished by this program, please enter a number
      corresponding to the task you want accomplished
1)Greet User
2)Sum Numbers
3)Perform a specified operation on unser-inputted numbers
4)Square user inputted number
5)Find the facotrial of a user inputted number
6)Count from a user provided start to a user prvided end
7)Find the hypotonuse of a right triangle, the user inputs its 
    side lengths
8)Squares user inputted number
9)Find the hypotonuse of a right triangle, the user inputs its 
    side lengths
10) find the area of a rectangle
11)raises a user inputed number to a user inputted power
12)returns the type of variable the user inputs""")
while is_valid == False:
    try:
        user_choice = int(input("Please pick a number:"))
        #raises an exception if the number is not in the 1-12 range
        if user_choice not in range(1,13):
            raise Exception("Not in range")
    except:
        #scolds user
        print("Input must be an integer between 1-12!")
    else:
        is_valid = True
#passes user_choice to the method number_to_method
vary.number_to_method(user_choice)

    




