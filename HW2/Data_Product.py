import pandas as pd
import random
import sklearn

# Classification Problem : Who is good master student
'''
feature information :
    ID : student id (integer)
    Hours(Hours in lab) : 4-10
    Age : 22-26
    Height : 150-180
    Weight : 40-80
    Gender : M, F
    Birthplace : north, middle, south, east
    Attitude : positive, negative
    Performance(Class performance) : great, good, normal, bad
    Sleeping(Average sleeping time) : 4-8
    Research time : 4-10
    Num of class : 2-5
    Entertainment : game, shopping, music
    Cost(Cost per day) : 150, 200, 250, 300
    Apple(Apple everyday) : True, False
    Freq_Sport(Freq of sports in one week) : 2, 3, 4
    Health : 1-5(bad to good)
    Label : 0(bad), 1(good)
absolute right rule : 
    Hours in lab : 8, 9, 10
    Attitude : positive
    Performance : great, good
    Research time : 6, 7, 8, 9, 10
'''
# feature = ['Hours', 'Age', 'Height', 'Weight', 'Gender', 'Birthplace',
#            'Attitude', 'Performance', 'Sleeping', 'Research time',
#            'Num of class', 'Entertainment', 'Cost', 'Apple', 'Freq_Sport',
#            'Health', 'Label']
feature = ['Age', 'Handsome','Height', 'Body Fat%', 'Crazy on work',
           'Attitude', 'Wage', 'Temper', 'Responsibility',
           'Have a cat', 'Ma bao', 'Have a car', 'Have a house', 'Have a rich dad',
           'Jai Jai', 'Label']
data = pd.DataFrame(columns=feature)
print(data)
# for i in range(450):
#     temp = [random.randint(22, 30), random.randint(0, 5), random.randint(160, 190),
#             random.randint(8, 35),random.choice([1,0]), 1,
#             random.randint(60000, 150000),
#             random.randint(4, 5), 1, random.choice([1,0]),
#             0, random.choice([1,0]), random.choice([1, 0]),
#             random.choice([1, 0]), random.choice([1, 0]), 1]
#     data.loc[i] = temp
count = 0
for i in range(10000):
    score = 0
    temp = [random.randint(22, 30), random.randint(0, 5), random.randint(160, 190),
            random.randint(8,35),random.choice([1,0]), random.choice([1, 0]),
            random.randint(25200,150000),random.randint(0, 5),
            random.choice([1,0]), random.choice([1,0]),
            random.choice([1,0]),random.choice([1,0]),random.choice([1,0]),
            random.choice([1,0]) , random.choice([1, 0]) ,]
    if(temp[5] == 1):#Attitude
        score += 3
    if (temp[5] == 0):#Attitude
        score += -1
    if(temp[6] > 130000):#wage
        score += 5
    elif (temp[6] > 100000):
        score += 3
    elif (temp[6] > 60000):
        score += 1
    if(temp[7] == 5):#Temper
        score += 2
    if (temp[7] == 4):
        score += 1
    if (temp[7] <= 2):
        score += -1
    if (temp[8] == 1): #Resposibility
        score += 3
    if (temp[10] == 1): #Ma bao
        score += -2
    if (temp[10] == 0):
        score += 1


    if(score >= 7):
        temp.append(1)
        count += 1
    else:
        temp.append(0)
    data.loc[i] = temp

print(count)
data_shuffled = sklearn.utils.shuffle(data)

print(data_shuffled)
print(data_shuffled['Label'].sum())
data_shuffled.to_csv('data.csv', index=False)
