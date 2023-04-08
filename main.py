import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
           'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
           'hours-per-week', 'native-country', 'income']
adult_data = pd.read_csv('data/adult.data.csv', names=columns)

print('============== sex ===============')
sex = adult_data['sex']

Male = [1 for x in sex if x == ' Male']
Female = [1 for x in sex if x == ' Female']

print('Male:', np.sum(Male))
print('Female:', np.sum(Female))

print('Male to Female ratio:', np.sum(Male) / np.sum(Female))
plt.figure(figsize=(10, 10))
plt.hist(sex)
plt.xlabel('gender')
plt.ylabel('count')
plt.title('Gender distribution in the dataset')
plt.savefig('sex.png')

print('============== age ===============')
age = adult_data['age']

print('Median:', np.median(age))
print('Mean:', np.mean(age))
print('Min:', np.min(age))
print('Maz:', np.max(age))

mean_age = age.mean()

plt.figure(figsize=(10, 10))
plt.hist(age, bins=20)
plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=2)
plt.xlabel('age')
plt.ylabel('count')
plt.title('Age distribution in the dataset')
plt.savefig('age.png')

print('============== income ===============')
income = adult_data['income']

LessThanOrEqual50K = [1 for x in income if x == ' <=50K']
GreaterThan50K = [1 for x in income if x == ' >50K']

print('<=50K:', np.sum(LessThanOrEqual50K))
print('>50K:', np.sum(GreaterThan50K))

plt.figure(figsize=(10, 10))
plt.hist(income)
plt.xlabel('income')
plt.ylabel('count')
plt.title('Income distribution in the dataset')
plt.savefig('income.png')

print('============== workclass ===============')
workclass = adult_data['workclass']
plt.figure(figsize=(10, 10))
plt.hist(workclass)
plt.xticks(rotation=30, ha="right")
plt.xlabel('workclass')
plt.ylabel('count')
plt.title('Workclass distribution in the dataset')
plt.savefig('workclass.png')

print('============== race ===============')
race = adult_data['race']
plt.figure(figsize=(10, 12))
plt.hist(race)
plt.xticks(rotation=30, ha="right")
plt.xlabel('race')
plt.ylabel('count')
plt.title('Race distribution in the dataset')
plt.savefig('race.png')

print('============== education ===============')
education = adult_data['education']
plt.figure(figsize=(10, 10))
plt.hist(education)
plt.xticks(rotation=30, ha="right")
plt.xlabel('education')
plt.ylabel('count')
plt.title('Education distribution in the dataset')
plt.savefig('education.png')

print('============== income, sex ===============')
LessThanOrEqual50KMale = 0
LessThanOrEqual50KFemale = 0

GreaterThan50KMale = 0
GreaterThan50KFemale = 0

for i in range(len(income)):
    if income[i] == ' <=50K' and sex[i] == ' Male':
        LessThanOrEqual50KMale += 1
    if income[i] == ' <=50K' and sex[i] == ' Female':
        LessThanOrEqual50KFemale += 1

    if income[i] == ' >50K' and sex[i] == ' Male':
        GreaterThan50KMale += 1
    if income[i] == ' >50K' and sex[i] == ' Female':
        GreaterThan50KFemale += 1

data = {'Male <=50K': LessThanOrEqual50KMale, 'Female <=50K': LessThanOrEqual50KFemale,
        'Male >50K': GreaterThan50KMale, 'Female >50K': GreaterThan50KFemale}

plt.figure(figsize=(10, 10))
plt.bar(data.keys(), data.values())
plt.xlabel('income,gender')
plt.ylabel('count')
plt.title('Income and Gender distribution in the dataset')
plt.savefig('income-sex.png')


print('============== occupation ===============')
occupation = adult_data['occupation']

plt.figure(figsize=(10, 10))
plt.hist(occupation)
plt.xticks(rotation=30, ha="right")
plt.xlabel('occupation')
plt.ylabel('count')
plt.title('Occupation distribution in the dataset')
plt.savefig('occupation.png')