a=[]
cnt=0
while True:
    n=int(input())
    if n==0: break
    a.append(n)
    if n%2==1 and n%3==0:
        cnt+=1
print(cnt, len(a))

