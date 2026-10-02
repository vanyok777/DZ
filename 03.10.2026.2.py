a=[]
cnt=0
N=1
while N!=0:
    N=int(input())
    a.append(N)
    if N%2==1 and N%3==0:
        cnt+=1
print(cnt, len(a)-1)
