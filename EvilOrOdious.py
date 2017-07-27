

def evil(n):
    b = []
    while n>0:
        rem  = n %2
        b.append(rem)
        n = n // 2

    k = 0

    for x in b:
        if x == 1:
            k += 1

    print(k)

    if k % 2 == 0:
        return 'It`s Evil!'

    else:
        return 'It`s Odious!'

def evilPro(n):
    return "It`s %s!" % ["Evil", "Odious"][bin(n).count("1")%2]

if __name__ == '__main__':
    print(evil(1))      #Odious
    print(evil(2))      #Odious
    print(evil(3))      #Evil