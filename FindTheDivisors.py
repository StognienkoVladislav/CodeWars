
def divisors(integer):
    n = []
    for i in range(integer):
        if integer % (i + 1) == 0:
            n.append(i + 1)

    if len(n) > 2:
        n.pop(0)
        n.pop()
        return n

    else:
        return "%s is prime" % n[1]


def divisorsPro(n):
    return [i for i in range(2, n) if not n % i] or '%d is prime' % n



if __name__ == '__main__':
    print(divisors(15), [3, 5])
    print(divisors(12), [2, 3, 4, 6])
    print(divisors(13), "13 is prime")