# start

# entering user name
try:
    user_name = str(input('Enter your name: '))
except:
    print("Oops, something goes wrong")

# welcoming info
print(f"Hello, {user_name} \nYou are here to solve the quest! Created by school subjects. Your goal is to answer all 12 questions in minimum time. All answears are numbers. You have 10 minutes and only 10 lives. \nTo start the game type \'GO\'. Good luck!")

# start message 
try:
    start = str((input('Type here: ')))
    start.lower()
    if start == 'go':
        print('3-2-1. Start!')
    else:
        exit()        
except:
    print('See you next time')
    exit()


# modules import
import datetime  #time
from questions import question   #questions list\
import random  # for random question 
from timer_countdown import timer


start_time = datetime.datetime.now()

# Timer for 10 min
target_time = 10 * 60

#start quiz
asked_questions = []
trial = 10
question_numbner = 0

for i in range(11):

    timer(start_time, target_time)

    x = 1    

    #question ID recalling
    while x == 1:
        idx = random.randrange(0,49)
        if idx not in asked_questions:
            asked_questions.append(idx)
            x = 0
            question_numbner += 1
            
    # asking a question
    try:
        user_answer = int(input(f"{question_numbner}. Subject: {question(idx, 'subject')} \n{question(idx, 'question')}"))
    except:
        print('Must be an integer')

    y = 1
    timer(start_time, target_time)

    while y == 1:

        if user_answer == question(idx, 'answer'): # if answer is correct
            y = 0
            timer(start_time, target_time)
            print (f'Correct! Go Ahead \n')
        else:
            trial -= 1                    # ask again, lives -1
            if trial == 0:
                print('No lives left. You loose. Try test again: ')
                exit()
            else:
                try:
                    user_answer = int(input(f'{trial} lives left. Try again: '))
                except:
                    print('Must be an integer')
                timer(start_time, target_time)
    
    end_time = datetime.datetime.now()

    
#final time definition
time_diff = end_time - start_time
time_res = round(time_diff.total_seconds())
time_min = round(time_res//60)
time_sec = time_res - 60 * time_min
   

print(f'WIN! You passed test for {time_min} min and {time_sec} sec with {trial} lives left')

    


        

            

        



 

