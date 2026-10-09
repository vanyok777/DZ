def main(a=int(input()), b=int(input())):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

num = [int(input()) for _ in range(3)]
g=num[0]
for x in num[1:]:
    g=main(g, x)
print(g)
