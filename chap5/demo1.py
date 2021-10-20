'''
age = 17
if age > 18:
    print("you are old enough to vote")
    print("have you registered to vote yet")
else:
    print("sorry,you are too young to vote")
    print("please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("your admission cost is 0")
elif age < 18:
    print("your admission cost is 5")
else:
    print("your admission cost is 10")

age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("your admission cost is " +str(price)+".")

alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print("玩家因射杀该外星人获得5个点")
else:
    print("玩家获得10个点")

requested_toppings = ['mushroom','green peppers','extra cheese']
if 'mushroom' == 'mushroom':
    print("sorry")
else:
    for requested_topping in requested_toppings:
        print("add " + requested_topping.title()+".")
print("finish")

requested_toppings = []
if requested_toppings:
     print("add " + requested_topping.title()+".")
else:
    print("sorry")
print("finish")
'''
available_toppings = ['mushroom', 'green peppers', 'extra cheese']
requested_toppings = ['mushroom', 'green peppers', 'extra cheese', 'tomato', 'potato']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("add " + requested_topping.title() + ".")
    else:
        print("sorry")
print("finish")

numbers = ['1st', '2nd', '3rd', '4', '5', '6', '7', '8', '9', '10', '11']
for num in range(1, 11):
    if num == 1:
        print(numbers[0])
    elif num == 2:
        print(numbers[1])
    elif num == 3:
        print(numbers[2])
    else:
        print(numbers[num-1]+"th.")
