def main(a=int(input()), b=int(input())):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

print(main())
