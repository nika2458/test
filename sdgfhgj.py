n = int(input("n = "))
m = int(input("m = "))
t = int(input("t = "))


def Blacktea(n, m):
    return n + m


def Difference(n, m):
    return n - m

def Product(n, m):
    return n * m


def Fraction(n, m):
    return n / m


if t == 1:
    r == Blacktea(n, m)
    print(r)

# я всё сказала == 2, 3, 4 уэуа елиф
# зделать ифы с т == 2, 3, 4 ииииииииииииии нужно елиф
elif t == 2:
    r == Difference(n, m)
    print(r)

elif t == 3:
    r == Product(n, m)
    print(r)

elif t == 4:
    r == Fraction(n, m)
    print(r)
else:
    print("`-`")