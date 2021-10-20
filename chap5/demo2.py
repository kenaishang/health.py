alien_0 = {
    'color': 'green',
    'points' :5
    }
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("you just earned "+str(new_points)+" points!")

alien_0 = {
    'color': 'green',
    'points' :5
    }
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25  #添加键值对
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)
del alien_0['color']
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'fast'
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
        x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new position: "+str(alien_0['x_position']))

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
print("Sarah favorite language is " + favorite_language['sarah'].title()+"!")

for key,value in favorite_language.items():
    print("\nkey: "+key)
    print("value: "+value+"\n")
    print(key.title()+"'s favorite language is "+ value.title() + ".\n")

for key in favorite_language.keys():
    print(key.title())
for value in favorite_language.values():
    print(value.title())

for name in favorite_language:
    print(name.title())

friends = ['edward', 'phil','tom']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("Hi,"+name.title()+"your favorite language is " +favorite_language[name].title() + "!")
    if 'tom' not in favorite_language.keys():
        print("\ntom,please take our poll!")
for name in sorted(favorite_language.keys()):
    print(name.title()+"thank you for taking the poll")

print("\nThe following language has been mentioned:")
for value in set(favorite_language.values()):
    print(value.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 155}
aliens = [alien_0 ,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens = []
#  创建30个外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed' :'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("~~~")
print("total number of aliens: "+str(len(aliens)))

pizza = {
    'crush': 'thick',
    'toppings': ['mushroom','extra cheese']
       }
print("You order a"+pizza['crush'] +"-crush pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)


favorite_languages = {
    'jen': ['python'],
    'sarah':  ['python','java','c'],
    'edward':  ['python','ruby','c'],
    'phil':  ['python'],
    }
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is ")
        print("\t"+languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite language are " )
        for language in languages:
            print("\t"+language.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
            },
    'mcurie': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    }
for username,user_info in users.items():
    print("username: "+username.title())
    print("\tinfoname: "+user_info['first'].title()+" "+user_info['last'].title())
    print("\tlocation: "+user_info['location'].title())

