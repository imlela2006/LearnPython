"""
Write a program ask user for
input a list of a comma separated numbers
Then go throw each element to calculate max & min
"""
s = input('Enter a list of a comma separated nums:\n')
str_nums = s.split(',')
print(str_nums)
num = []

for n in str_nums:
    num.append(int(n))
print(num)
nums = list(map(max,int)(s))
print(max)
nums = list(map(min,(int)(s))
print(min)