def parse_float(string):
    try:
        float(string)
        return float(string)
    except:
        return None



if __name__ == '__main__':

    ts = (
        ("1.0", 1.0),
        ("a", None),
        ("234.0234", 234.0234)
    )

    for t in ts:
        print(parse_float(t[0]), t[1])