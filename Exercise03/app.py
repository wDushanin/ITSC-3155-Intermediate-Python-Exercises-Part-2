
# Title: Module_03 Intermediate Python Exercises(2) Exercise #3
# Author: Wendy Dushanin
# UNCC Student ID: 800727084
# Date: February 24, 2022

# Description:
# Create a virtual environment (with any name) and activate it. Install the requests library (Links to an external site.) 
# which is used to make HTTP requests to HTTP servers, just like a web browser can do. Remember to create your requirements.txt
#  file after installing 3rd party modules in a virtual environment. Use the requests library to print out the HTML source code 
# of https://www.charlotte.edu/ (Links to an external site.). If you get stuck, check out this page in the docs 
# (Links to an external site.) and this YouTube video (Links to an external site.) (feel free to watch all of it to learn more, 
# but you should only need the first five minutes or so). Remember do not commit the environment directory created by venv but 
# do commit the requirements.txt file.

# References: 
# https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# http://bluegalaxy.info/codewalk/2017/09/21/python-using-requests-to-get-web-page-source-text/
# https://www.youtube.com/watch?v=tb8gHvYlCFs&ab_channel=CoreySchafer 

import requests

r = requests.get('https://www.charlotte.edu')

source = r.text[:500] #Limit response to first 500 characters b/c not limiting resulted in an overwhelming output

print(source)