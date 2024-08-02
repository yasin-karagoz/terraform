import logging

print("200 is a number") # String
print(3.5) # Float
print(3) # Integer

print(20 * 24 * 60) # arithmetic Operators

##### String Concatenation ### Gluing together #only in python 3
print("20 days are " + str(50) + " minutes")
print(f"20 days are {50} minutes") # cleaner
print(f"20 days are {20 * 24 * 60} minutes") #f stands for formatting

#### Veriables ####
print(f"20 days are {20 * 24 * 60} minutes")
calculation_to_units = 24  #example
name_of_unit = "hours"
print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"10 days are {10 * calculation_to_units} {name_of_unit}")
print(f"25 days are {25 * calculation_to_units} {name_of_unit}")
#reserverd words can't be use for veriables

### Functions ###
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units():  #Functions should be indented
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units() #calling the function

### Function Paramaters ###

def days_to_units(number_of_days, custom_message):   #input paramater #you can define as many input parameter as you want
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}") #input paramater veriable may replace with number
    print("custom_message")

days_to_units(35) #defining the number
days_to_units(20, "Awesome") #for 2 input paramater on the above
days_to_units(25)
days_to_units(31)

### Scope ###  global scope= outside the function local veriable scope = inside the function

def scope_check(num_of_days):
    my_var = "veriable inside function" #internal veriable
    print(name_of_unit) #globel veriable
    print(num_of_days) #local veriable

scope_check(20)

### User Input ### ask for add allow to user input built in function

def days_to_units(number_of_days, custom_message):   #input paramater #you can define as many input parameter as you want
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}") #input paramater veriable may replace with number
    print("custom_message")

user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
print(user_input)


#### Function with Return Values ###

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):   #input paramater #you can define as many input parameter as you want
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
user_input_number = int(user_input)  ##casting turning the value one data type another type

calculated_value = days_to_units(user_input_number)
print(calculated_value)

### Conditionals (if /else) & Boolen Data Type

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(number_of_days):   #input paramater #you can define as many input parameter as you want
    condition_check = number_of_days > 0
    print(type(condition_check))

    if number_of_days > 0:  #if conditions are intented  ##Condition is TRUE or FALSE
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number
    else:
        return "you entered a negative value, so no conversion for you"

user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)



def days_to_units(number_of_days):   #input paramater #you can define as many input parameter as you want
    if number_of_days > 0:  #if conditions are intented  ##Condition is TRUE or FALSE
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number
    elif number_of_days == 0: ## used two == because one = is already used
        return "entered 0, enter positive number"
    else:
        return "you entered a negative value, so no conversion for you"

user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)

### More User Input Validation for Text inputs and float number
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):   #input paramater #you can define as many input parameter as you want
    if number_of_days > 0:  #if conditions are intented  ##Condition is TRUE or FALSE
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number
    elif number_of_days == 0: ## used two == because one = is already used
        return "entered 0, enter positive number"

user_input = input("hey user, enter a number of days and I'll convert it to hours\n")

if user_input.isdigit():     ###paramater
    user_input_number = int(user_input)
    calculated_value = days_to_units(user_input_number)
    print(calculated_value)
else:
    print("your input is not a valid number. Don't ruin the app")

### Clean up in main.py
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number
    elif number_of_days == 0:
        return "entered 0, enter positive number"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("your input is not a valid number. Don't ruin the app")


user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
validate_and_execute()


### Nested If... Else  it will clean the code below

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
    else:
        print("your input is not a valid number. Don't ruin the app")


user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
validate_and_execute()


###### Error Handling with try/except

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")


user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
validate_and_execute()


#### While Loops   continue aftyer its caltculated first value 2 loop commands

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")

while True:
    user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
    validate_and_execute()


#### Let User exit the program

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")

user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter a number of days and I'll convert it to hours\n")
    validate_and_execute()

### Lists & For Loop  Data type=Lists
#Data types so far
# String -Float -Integer -Boolean -Lists
"String example"
10
19.99
True
False
[10, 15, 40, 100]

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")

user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter number of days as a comma separated list I'll convert it to hours\n")
    print(type(user_input.split(",")))  ##you can see type it will show class, list
    print(user_input.split(","))
    for num_of_days_element in user_input.split(", "): #it will list values user_input in terminal
        validate_and_execute()

#### Basic List Operations

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")

user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter number of days as a comma separated list I'll convert it to hours\n")
    print(type(user_input.split(",")))  ##you can see type it will show class, list
    print(user_input.split(","))
    for num_of_days_element in user_input.split(", "): #it will list values user_input in terminal
        validate_and_execute()

### List example
my_list = ["January", "February", "march"]
my_list[0]        ### Index element starts with 0 and goes 0 1 2
print(my_list[2])  ### You can access only march
my_list.append("April") #It will add April at the end of the list
print(my_list[3]) #it will print out last added element

### Comments => give yourself Notes in your code

"""multi line comments """


### Sets ==>

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}" #input paramater veriable may replace with number


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")

user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter number of days as a comma separated list I'll convert it to hours\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days))) # order goes from set to print

    for num_of_days_element in set(user_input.split(", ")): #it will list values user_input in terminal
        validate_and_execute()

### Basic Set Operations & Syntax
###Set examples
my_set = {"January", "February", "March"} # you need to call it in for loop
for element in my_set
    print(element)

my_set.add("April") # set has built in functions as add its not like list # order is random when you call it
print(my_set)

my_set.remove("January") # you can remove element with built in function also same function in list
print(my_set)

### Built in Functions

# Functions we used so far
print("some text")  # Prints to the standard output device
input("enter value")  # Asks user for input
set([1, 2, 5])    # Returns a new set
int("20")    # Converts value into an integer

"2, 3".split()  ## This is also built in functions on the value
"text".upper()  ### Truns this text to Upper


### Dictionary Data Type
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return: "unsupported unit"

def validate_and_execute():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:             #### Nested elif
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:          ### Nested elif
            print("entered 0, enter positive number")
        else:
            print("negative number, no conversion")
    except ValueError:   ## Diffierence with if-else to try-except try except with ValueError will cover Value type of error #another way is try and catch
        print("your input is not a valid number. Don't ruin the app")

user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter number of days as a conversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]} ### Syntax of dictionary
    validate_and_execute()


"""my_list = ["20", "30", "100"]
print(my_list[2])

my_dictionary = {"days": 20, "unit": "hours"}
print(my_dictionary["unit"])"""


### Data types learned so far
message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_input = Flase
list_of_days = [20, 40, 30]
list_of_months = ["january", "February", "June"]
set_of_days = {20, 45 ,100}
days_and_unit  = {"days": 10, "unit": "hours"}


### Modules  is just a .py file you can reference one module(file) to another

## Create a Module & import statement
##import helper file to main.py
## helper.validate_and_execute() add helper file to execute function, it will take from helper file
## In helper.py def validate_and_execute(days_and_unit_dictionary): need to added veriable and in main.py
## we need to add helper.validate_and_execute(days_and_unit_dictionary) veribale

## If you need to import only one funcion you can also call only function in helper as
## from helper import validate_and_execute and validate_and_execute(days_and_unit_dictionary)


### Built in Python Modules
## Examples
##import os ## for OS

## import logging for Logging
logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")


### Project Now as Countdown App
# in time-till-deadline.py

### modules and packages
#pypi.org

### Pip
#pip install package


### Automation with Python
### Project with spreadsheet
# We installed the spreadsheet package pip install openpyxl
## implementation

### Classes and Objects
#create a Class
class User:
    def __init__(self):  # => #self is a reference to currebt instance of the class


# Create Object
User() # => calling the User class
## Functions belongs to Class are called Methods

class User:
    def __int__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):  # change_password is method
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title


User("yk@com", "Yasin Karagoz", "pwd1", "DevOps Engineer")


### Classes in files are objets and main file will create objects.

### Obeject orianted programing

