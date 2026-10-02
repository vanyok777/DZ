n=int(input())
a=[]
cnt=0
for i in range(n):
    N=int(input())
    a.append(N)
    if N%4==0:
        cnt+=1
print(cnt)
