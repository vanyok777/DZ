n1=0.1
n2=0
for i in range(100):
    n2=(i+1)/10
    print(f'{n1}=={n2} equals {n1==n2}')
    n1+=0.1
