# Title: Module_03 Intermediate Python Exercises(2) Exercise #2
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 1, 2022

# Description: 
# Take in 5 int inputs from the user and add them together. The catch is that you
# can no longer assume that what the user enters is a valid int. If the user enters
# an invalid input, print an error message and make the user input the int again
# until all 5 int values are entered correctly. Print the resulting sum.

# References: 
# https://www.javatpoint.com/python-display-fibonacci-sequence-recursion
# https://datatofish.com/measure-time-to-run-python-script/

import time

#Function to calculate number in fibonacci sequence using recursion 
def find_fib(x):
    if x <= 1: 
        return x
    else:
        return(find_fib(x-1) + find_fib(x-2)) #This is recursion--the function calls on itself inside itself


#Test Code
startTime = time.time() #gets the current time and stores it in 'startTime'
num = find_fib(35) #hard coding the number 35 into the function call
print(f'fib(35) = {num}') #printing the result
executionTime = (time.time() - startTime) #gets the current time after running the function call.  Time now - start time = total execution time
print(f'fib(35) took {executionTime} seconds') #print the amount of seconds it took for the function call to run