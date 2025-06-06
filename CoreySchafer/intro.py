
# import my_module
# from my_module import * # Imports everything
import my_module as mm # Importing as a shot form
from my_module import find_index, test # Imports the function alone and test variable
# from my_module import find_index as fi, test # Imports the function alone and test variable
courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
# index = my_module.find_index(courses, 'Math')
index = find_index(courses, 'Math')
# index = fi(courses, 'Math')
print(index)
print(test)

print()
# Knowing how it access the imort
import sys
print(sys.path)
print()
print(f'========================================================')
import random

random_number = random.randint(1, 20)
print(f'Random Number is: {random_number}')
print()
random_course = random.choice(courses)
print(f'The random course from the list is: {random_course}\n')
random_range = random.randrange(20, 30)
print(f'The random range is: {random_range} \n')

import math
# Converting degrees to radians

rads = math.radians(90) # Converts degrees to radians
sine = math.sin(rads) # Converts to sine
print(f'90° to radians is: {rads} \n')
print(f'The sine of 90° is {sine}\n')

import datetime
import calendar

today = datetime.date.today()
print(today, '\n')
print(calendar.isleap(2017), '\n')

import os
# gives us access to the underlying operating system

print(os.getcwd(), '\n') # print current working directory
print(os.__file__, '\n') # To find the location of an  module...print its dunder file method

import antigravity

# The above opens the following browser: https://xkcd.com/353/
import sys
print(sys.executable)
print(sys.version)
print()
class Employee:
    """ A Sample Employee class """
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f'{self.first}, {self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first}, {self.last}.'
    
emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print()
for num in [1,2,3,4, 5]:
    print(num)

print()
emp_2 = Employee('Kelvin', 'Durant')

# Python extensions
# Auto pep 8
# Auto Django
# Linter-flake8   =====> pip install fl# ake8
# GlassIt
# Live Server
# file icons or VsCode Great Icons or vscode-icons 

# mkdir my_project
# cd my_project/
# conda create --name my_project_env flask sqlalchemy numpy pandas
# y/n   ===> y
''' Activate the environment'''
# source activate my_project_env 
''' DeActivate the environment'''

# source deactivate my_project_env
# pip list 
# yaml file to create an environmentment

# conda env export > environment.yaml    
# 
# zips the environment in a yaml filecreates a yaml environment

# cat environment.yaml
# clear
# conda env create -f environment.yaml  

# The above code is for someone who wants to create or replicate that 
# same environment in a different place or project.

# conda env list

# mkdir -p etc/conda/activate.d
    # touch etc/conda/activate.d/env_vars.sh 
'''''   #!/bin/sh
        export DATABASE_URI="postgresql://user:pass@db_server:5432/test_db"
'''''
# mkdir -p etc/conda/deactivate.d
    # touch etc/conda/deactivate.d/env_vars.sh 
'''''   #!/bin/sh
        unset DATABASE_URI     
'''''
# source activate
# source deactivate

# echo $DATABASE_URI





