
def duplicate_count(text):
    k = 0
    i=1
    z = 0
    for x in range(0, (text.__len__() ), 1):
        if x == " ":
            continue
        for j in range(i, (text.__len__() ), 1):
            if text[j] == text[x]:
                k += 1
                text.replace(text[j], " ")
            i +=1
        if k > 0:
            z +=1
            k = 0
    return (z)


if __name__ == '__main__':

    print(duplicate_count("abcde"), 0)
    print(duplicate_count("abcdea"), 1)
    print(duplicate_count("indivisibility"), 1)