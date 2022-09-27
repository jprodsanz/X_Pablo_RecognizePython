# variable declaration
num1 = 42
num2 = 2.3

#data type boolean 
boolean = True

#log statement 
string = 'Hello World'

#list of toppings in an array 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

#list of attributes 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# tuple list 
fruit = ('blueberry', 'strawberry', 'banana')

#log statement 
print(type(fruit))
#log statement 
print(pizza_toppings[1])
#log statement 
pizza_toppings.append('Mushrooms')
#log statement 
print(person['name'])
#log statement 
person['name'] = 'George'
#log statement 
person['eye_color'] = 'blue'
#log statement 
print(fruit[2])


#conditionals if / else if / else 
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop 
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

#delete value 
pizza_toppings.pop()
pizza_toppings.pop(1)

# add value 
print(person)
person.pop('eye_color')
print(person)

# for loop increment 
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# for loop 
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
#function 
print(num3)

#variable declaration
num3 = 72

#index locator 
fruit[0] = 'cranberry'

#log statement
print(person['favorite_team'])

print(pizza_toppings[7])

#true or false statement 
print(boolean)

fruit.append('raspberry')

fruit.pop(1)

                                                # Solution

num1 = 42  # variable declaration, number initialized 
num2 = 2.3 # variable declaration, decimal/float initialized
boolean = True # variable declaration, boolean initialized
string = 'Hello World' # variable declaration, string initialized

# variable declaration, list initialized 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, dic initialized  
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, tuple initialized 
fruit = ('blueberry', 'strawberry', 'banana')

# print to console, type check 
print(type(fruit))

# print to console, List access value 
print(pizza_toppings[1])

# list add value 
pizza_toppings.append('Mushrooms')

# print to console, Dic access value  
print(person['name'])

# Dictionary Change value 
person['name'] = 'George'
# Dictionary Change Value 
person['eye_color'] = 'blue'

# print to console, Tuple access data 
print(fruit[2])


# Conditional if, evaluation, print to console, Conditional else, print to console

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Conditional if - elif - else, print to console 
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# For Loop start at 0 and goes up to until 5 
for x in range(5):
    print(x)
# For Loop start at 2 and goes up to until 5
for x in range(2,5):
    print(x)
# For loop start at 2 goes up to until 10, increments by 3 
for x in range(2,10,3):
    print(x)


# WHile Loop, variable declaration
x = 0
while(x < 5):
    # printing to console 
    print(x)
    # incrementing x
    x += 1

# List delete value at end 
pizza_toppings.pop()

# List delete value at index 
pizza_toppings.pop(1)

# print to console of dictionary
print(person)
# Dictionary delete value 
person.pop('eye_color')
# print to console of dictionary  
print(person)

# for loop through a list 
for topping in pizza_toppings:
    # Conditional if 
    if topping == 'Pepperoni':
    # Continues 
        continue
    #Print to console 
    print('After 1st if statement')
    # Conditional if 
    if topping == 'Olives':
    # stops the loop 
        break

# function declaration 
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

# Function Call 
print_hello_ten_times()

# Function Declaration with parameter x 
def print_hello_x_times(x):
    # For loop up until a given number x 
    for num in range(x):
        # print to console 
        print('Hello')

# function call argument of 4 
print_hello_x_times(4)

# function declaration with default parameter 
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

# function call goes to 10 
print_hello_x_or_ten_times()
# function call goes to 4 
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# print variable num3
print(num3)
num3 = 72

# list access by index 
fruit[0] = 'cranberry'

# concatenation of two variables in this case person + favorite_team 
print(person['favorite_team'])

# print to console pizza toping of index 7 
print(pizza_toppings[7])

# print true or false statement yes or no type of question, ya dig? 
print(boolean)

# add to list 
fruit.append('raspberry')
# delete from list 
fruit.pop(1)