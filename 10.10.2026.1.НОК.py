def main(a=int(input()), b=int(input())):
    a, b = abs(a), abs(b)
    x=a*b
    while b != 0:
        a, b = b, a % b
    return x/a

print(main())
