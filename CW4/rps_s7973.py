import numpy as np
import time

a = np.random.random()
b = np.random.random()
c = np.random.random()
start = ['Paper','Rock','Scissors']
p_start = [(1-a)/2,a,(1-a)/2]
t1 = ['Paper','Rock','Scissors']
p_t1=[[(1-c)/2,(1-c)/2,c],[(1-c)/2,c,(1-c)/2],[c,(1-c)/2,(1-c)/2]]
p_t2=[(1-b)/2,b,(1-b)/2]
comp_score = 0
user_score = 0
initial = np.random.choice(start,replace=True,p=p_start)
activityList = [[],[]]
activityList[0].append("You")
activityList[1].append("Computer")
state = initial
n = 10
st = 1
for i in range(n):
    if state == 'Paper':
        activity = np.random.choice(t1,p=p_t2)
        print(state)
        print(activity)
        if activity == 'Scisors':
            user_score = user_score - 1
            comp_score = comp_score + 1
            p_t1[0][1] = p_t1[0][1] + (1 - p_t1[0][1])/2
            p_t1[0][2] = (1 - p_t1[0][1])/2
            p_t1[0][0] = (1 - p_t1[0][1])/2
            print("COMPUTER WON!")
        elif activity == 'Rock':
            user_score = user_score + 1
            comp_score = comp_score - 1
            print("YOU WON!")
        else:
            print("TIE!")
        activityList[0].append(state)
        activityList[1].append(activity)
        state = np.random.choice(t1,p=p_t1[1])
    elif state == 'Rock':
        activity = np.random.choice(t1,p=p_t2)
        print(state)
        print(activity)
        if activity == 'Paper':
            comp_score = comp_score + 1
            user_score = user_score - 1
            p_t1[1][2] = p_t1[1][2] + (1- p_t1[1][2])/2
            p_t1[1][0] = (1 - p_t1[1][2])/2
            p_t1[1][1] = (1 - p_t1[1][2])/2
            print("COMPUTER WON!")
        elif activity == 'Scisors':
            comp_score = comp_score - 1
            user_score = user_score + 1
            print("YOU WON!")
        else:
            print("TIE!")
        activityList[0].append(state)
        activityList[1].append(activity)
        state = np.random.choice(t1,p=p_t1[1])
    elif state == 'Scissors':
        activity = np.random.choice(t1,p=p_t2)
        print(state)
        print(activity)
        if activity == 'Rock':
            comp_score = comp_score + 1
            user_score = user_score - 1
            p_t1[2][0] = p_t1[2][0] + (1- p_t1[2][0])/2
            p_t1[2][1] = (1 - p_t1[2][0])/2
            p_t1[2][2] = (1 - p_t1[2][0])/2
            print("COMPUTER WON!")
        elif activity == 'Paper':
            comp_score = comp_score - 1
            user_score = user_score + 1
            print("YOU WON!")
        else:
            print("TIE!")
        activityList[0].append(state)
        activityList[1].append(activity)
        state = np.random.choice(t1,p=p_t1[2])
    print("\n")
    time.sleep(0.5)
print("This game")
for i in range(n):
    print(activityList[0][i] + "     " + activityList[1][i])
print()
print("Computer score: ")
print(comp_score)
print("Your score: ")
print(user_score)
  
