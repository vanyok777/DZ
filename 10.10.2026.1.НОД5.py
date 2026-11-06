def main(a=int(input()), b=int(input()), c=int(input()), d=int(input()), e=int(input())):
    a, b, c, d, e = abs(a), abs(b), abs(c), abs(d), abs(e)

    while b != 0:
        a, b = b, a % b

    while c != 0:
        a, c = c, a % c

    while d != 0:
        a, d = d, a % d

    while e != 0:
        a, e = e, a % e

    return a

print(main())