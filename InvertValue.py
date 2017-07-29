
def invert(lst):
    if len(lst) == 0:
        return lst

    else:
        k=0
        for x in lst:
            lst[k] = -x
            k+=1
        return lst




if __name__ == '__main__':
    print(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
    print(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
    print(invert([]), [])
    print(invert([-739, 286, -735, 937, -201, 169, -788, -897, 363, 470, -881, 24, 637, -320, 665, 744, -951, 472, 478, 902, 817, -483, 715, -963, -772, -253, 499, 822, 640, -697, -430, -169, 162, 67]))
