
def triple_trouble(one, two, three):
    x = ''
    for i, j, k in zip(one, two, three):
        x += i + j + k
    return x

if __name__ == '__main__':
    print(triple_trouble("aaa", "bbb", "ccc"), "abcabcabc")
    print(triple_trouble("aaa", "bbb", "ccc"), "abcabcabc")
    print(triple_trouble("aaaaaa", "bbbbbb", "cccccc"), "abcabcabcabcabcabc")
    print(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
    print(triple_trouble("Bm", "aa", "tn"), "Batman")
    print(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")

