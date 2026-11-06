def main(a=int(input()), b=int(input()), c=int(input())):
    a, b, c = abs(a), abs(b), abs(c)

    while b != 0:
        a, b = b, a % b

    while c != 0:
        a, c = c, a % c

    return a

print(main())