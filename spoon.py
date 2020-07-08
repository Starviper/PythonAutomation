while True:
    print ('Who are you?')
    name = input()
    if name != 'Jared':
        continue
    print('Hello, Jared. What is the password? (hint: Matrix Ref.)')
    password = input()
    if password == 'thereisnospoon':
        break
print('Access Granted')
