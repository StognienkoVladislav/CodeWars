def scratch(lottery):
    #your code here
    sum = 0

    for x in lottery:
        j = x.split()
        if j[0] == j[1] == j[2]:
            sum += int(j[3])
    return sum


def scratchPro(lottery):
    return sum(int(x.split(' ')[3]) for x in lottery if len(set(x.split(' ')[:3])) == 1)
    #set - контейнер с неповтор элементами





if __name__ == '__main__':
    print((scratch(
        ["tiger tiger tiger 100", "rabbit dragon snake 100", "rat ox pig 1000", "dog cock sheep 10",
         "horse monkey rat 5", "dog dog dog 1000"]), 1100))