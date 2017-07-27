def remove(s):
    try:
        if s[-1] == '!':

            return s[0: -1]
        else:
            return s

    except:
        return ''

def removePro(s):
    return s[:-1] if s.endswith('!') else s


if __name__ == '__main__':
    tests = [
        # [input, [expected]],
        ["Hi!", "Hi"],
        ["Hi!!!", "Hi!!"],
        ["!Hi", "!Hi"],
        ["!Hi!", "!Hi"],
        ["Hi! Hi!", "Hi! Hi"],
        ["Hi", "Hi"],
    ]

    for inp, exp in tests:
        print(remove(inp), exp)