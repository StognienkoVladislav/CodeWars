

def fire_and_fury(tweet):

    test = tweet.replace("FIRE", "0").replace("FURY", "1")
    test_str = ""

    for x in test:
        if x == "0" or x == "1":
            test_str += x

    print(test_str)

    print(tweet)
    lst = {}
    n = 0
    for i in range(test_str.__sizeof__()):

        try:
            if test_str[i] == test_str[i+1]:
                n += 1

            else:
                n = 0
        except:
            raise

        lst[i] = n

    for x, y in lst.items():
        print(x + " " + y)

    return "Fake tweet."






if __name__ == '__main__':
    print("Sample tests")
    print("Ex1")
    print(fire_and_fury("FURYYYFIREYYFIRE"), "I am furious. You and you are fired!")
    print('<COMPLETEDIN::>')

    print("\nEx2")
    print(fire_and_fury("FIREYYFURYYFURYYFURRYFIRE"), "You are fired! I am really furious. You are fired!")
    print('<COMPLETEDIN::>')

    print("\nEx3")
    print(fire_and_fury("FYRYFIRUFIRUFURE"), "Fake tweet.")
    print('<COMPLETEDIN::>')
    print('<COMPLETEDIN::>')