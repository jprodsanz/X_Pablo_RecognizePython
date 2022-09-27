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