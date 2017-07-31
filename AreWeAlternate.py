

def is_alt(s):
    n = ['a', 'e', 'i', 'o', 'u']
    b = True

    if s[0] in n:
        for j in range(0, s.__len__() - 1, 2):
            if s[j] not in n:
                b = False
                break
    else:
        for j in range(1, s.__len__() - 1, 2):
            if s[j] not in n:
                b = False
                break

    return b



if __name__ == '__main__':
    print(is_alt("amazon"), True)
    print(is_alt("apple"), False)
    print(is_alt("banana"), True)
    print(is_alt("orange"), False)
    print(is_alt("helipad"), True)
    print(is_alt("yay"), True)