import random, sys

while True:
    print('What is your Question? q to exit.' )
    Question = input()
    def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        elif answerNumber == 3:
            return 'Yes'
        elif answerNumber == 4:
            return 'Reply hazy try again'
        elif answerNumber == 5:
            return 'Concentrate and ask again'
        elif answerNumber == 7:
            return 'my reply is no'
        elif answerNumber == 8:
            return 'Outlook not so good'
        elif answerNumber == 9:
            return 'Very doubtful'
    if Question == 'q':
        sys.exit()
    elif Question != 'q':
        print(getAnswer(random.randint(1,9)))
