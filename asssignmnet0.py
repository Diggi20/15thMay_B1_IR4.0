##question-1

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]
for i in numbers:
    if i%2==0:
        print(i)
    elif(i==237):
        break

##question-2

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

##question-3

import string
n = input('Enter a sentence to check if its a pangram or not: ')
def pangram(n):
    return set(string.ascii_lowercase)-set(n.lower())==set([])
if pangram(n)==True:
    print('The string is pangram')
else:
    print('The string is not pangram')

##question-4

a = int(input('Enter a number: '))
print('Result: ',(a + ((a*10)+a) + (a*100)+((a*10)+a)))

##question-5

b = input('Enter the string: ')
result = b.split('#')
list1 = [int(i) for i in list(result[0].split())]
list2 = [int(i) for i in list(result[1].split())]
print('x =',list1)
print('y =',list2)

##question-6

c = input('Enter words separated ny comma: ')
c_list = c.split(',')
c_list.sort()
print((', '.join(c_list)))

##question-7

d ={'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
result=0
for i in d['Marks']:
    if (i==max(d['Marks'])):
        break
    elif(i!=max(d['Marks'])):
        result +=1
print(d['Student'][result])


##question-8

w = input('Enter a sentence: ')
letter,digit = 0,0
for i in w:
    if i.isdigit():
        digit += 1
    elif (i.isalpha()):
        letter +=1
    else:
        pass
print('LETTERS ',letter)
print('DIGITS ',digit)


##question-9

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
n = input('Enter Subject: ')
lst1 = []
newdata = {}
for i in range(len(d['Subject'])):
    if(d['Subject'][i]!=n):
        continue
    else:
        lst1.append(i)
newdata['Name'] = []
newdata['Subject'] = []
newdata['Ratings'] = []
for i in lst1:
    newdata['Name'].append(d['Name'][i])
    newdata['Subject'].append(d['Subject'][i])
    newdata['Ratings'].append(d['Ratings'][i])
print('newData =',newdata)


##question-10


n = int(input('Enter a number for a range from o to '))
def gnrtrfunc(n):
    for i in range(1,n+1):
        if i%7==0:
            yield i
        else:
            continue
for x in gnrtrfunc(n):
    print(x)


##question-11


lst1= []
x = None
print('Enter direction and route(format is DIRECTION<space>STEPS):')
for _ in range(0,4):
    s = input('')
    x = s.split(' ')
    lst1.append(x)
us = 0
ds = 0
ls = 0
rs = 0

for i in lst1:
    if i[0].upper() == 'UP':
        us = int(i[1]) 
    elif i[0].upper() == 'DOWN':
        ds = int(i[1])
    elif i[0].upper() == 'LEFT':
        ls = int(i[1])
    elif i[0].upper() == 'RIGHT':
        rs = int(i[1])

z = us-ds
y = ls-rs

print(z)
print(y)

d = round(abs(((z**2)+(y**2))**0.5))
print(d)

    

    
