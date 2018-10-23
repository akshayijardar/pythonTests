message = """Aki's World
knkfdjghkgh"""
new_message = message.replace('Aki','Teju')

greeting = "Hello"
name="Akshay"
command="Welcome!"



print(message)
print(len(message))
print(message[-15:23])
print(message.lower())
print(message.upper())
print(message.count('b'))
print(message.find('World'))
print(message.find('life'))
print(new_message)

message = greeting +" "+ name+ " "+command
print(message)

message= '{} {}, {}'.format(greeting, name, command)
print(message)

message=f'{greeting.lower()} {name.upper()} {command}'
print(message)