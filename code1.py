#Question1
str1="python"
r_str1=" "
for i in range(len(str1)-1,-1,-1):
    r_str1 +=str1[i] 
print('Reversed String:', r_str1)

#question 2
my_list = ['apple', 30,'grape','mango',90, 100,70,'onion']
n=len(my_list)
i=1
while i<n:
    print('index', i,'=',my_list[i])
    i+=2

#question 3
print(type(my_list))

#Question 4
str2 =input('enter the string:')
vowel1 =['a','e','i','o','u']
x=" "
n=len(str2)
for i in range(n):
    if str2[i] not in vowel1:
        x += str2[i]
print('without vowel string:',x)

#Question5
str3 = input('enter the string:')
y=" "
m = len(str3)
for j in range(m):
    if str3[j].isalpha(): 
        y += str3[j]
print('New string is:',y)
