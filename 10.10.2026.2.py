n=int(input())
b=[]
for i in range(n):
    a=int(input())
    if a%7==5:           # Последняя цифра числа в семяричной равна остатку от деления числа на 7
        b.append(a)

if len(b)==0:
    print("No")
else:
    print(sum(b)/len(b)) # Можно сделать, не используя списков, но так проще
