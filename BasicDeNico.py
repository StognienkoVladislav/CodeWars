
def de_nico(key, msg):
    n = [[] for i in range(len(key))]
    pkey = key
    #print(pkey)
    key = sorted(key)

    #print(key)
    #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')

    l=0
    for x in key:
        n[l].append(x)
        l += 1
    print(n)

    #y = msg.replace(" ", "")
    #print(y)

    t=0
    for z in msg:
        if t > (len(key) - 1):          # запись в лист
            t = 0
        n[t].append(z)
        t+=1

    print(n)

    msg = ""

    #for x in n:
    #    for k in range(len(n[x])):  #Лист листов
    #        msg += x[k+1]

    z = 1

    r = []

    for j in pkey:                      #Swap Относительно ключа
        for y in n:
            if j == y[0]:
                r.append(y)

    print(r)



    for j in range(r[0].__len__() - 1):
        for x in r:
            msg += x[j+1]

    return msg.replace(" ", "")



if __name__ == '__main__':
    print(de_nico("crazy", "cseerntiofarmit on  "))
    #print(de_nico("crazy", "cseerntiofarmit on"), "secretinformation")
    #print(de_nico("abc", "abcd"), "abcd")
    #print(de_nico("ba", "2143658709"), "1234567890")
    #print(de_nico("a", "message"), "message")
    #print(de_nico("key", "eky"), "key")