
def de_nico(key, msg):
    n = [[] for i in range(len(key))]

    l=0
    for x in key:
        n[l].append(x)
        l += 1

    y = msg.replace(" ", "")
    y = y.split()

    for z in y:
        for j in range(len(key)):
            n[j].append(z)

    n.sort()

    msg = ""

    for x in range(len(key)):
        for k in range(len(n[x])):
            msg += n[x[k]]

    return msg



if __name__ == '__main__':
    print(de_nico("crazy", "cseerntiofarmit on  "), "secretinformation")
    print(de_nico("crazy", "cseerntiofarmit on"), "secretinformation")
    print(de_nico("abc", "abcd"), "abcd")
    print(de_nico("ba", "2143658709"), "1234567890")
    print(de_nico("a", "message"), "message")
    print(de_nico("key", "eky"), "key")