import random, sys

while True:
    print('What is your question? type q to exit')
    question = input()
    if question == 'q':
        sys.exit()
    
    messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
    print(messages[random.randint(0, len(messages) -1)])
