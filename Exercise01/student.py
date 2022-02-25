
# Title: Module_03 Intermediate Python Exercises(2) Exercise #1
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 24, 2022

# Description:
# Create a file called "student.py" and create a Student class. The Student class should have a constructor that takes in a 
# name and GPA and stores them both as instance fields. Create a report_gpa method which returns a string 
# (does not print out, just returns) that says "{name} has a GPA of {gpa}". In a separate file (you can just call it "app.py"), 
# import the Student class, instantiate it with a hardcoded name and GPA, and print out the result of calling the report_gpa method on
# that class instance.

# References: 
# https://www.geeksforgeeks.org/python-classes-and-objects/
# https://www.w3schools.com/python/python_classes.asp

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def report_gpa(self):
        report = (f'{self.name} has a GPA of {self.gpa}.')
        return(report)