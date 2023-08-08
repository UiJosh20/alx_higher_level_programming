#!/urs/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    elif b % 2 == 0:
        temp = pow(a, b // 2)
        return temp * temp
    else:
        return a * pow(a, b - 1)
