def band_name_generator(name):
    if  name[0] == name[-1]:
        a = "%s%s%s" % (name[0].upper(),name[1:],name[1:])
        return a

    else:
        a = "The %s%s" % (name[0].upper(),name[1:])
        return a


if __name__ == '__main__':
    print(band_name_generator('knife'), "The Knife")
    print(band_name_generator('tart'), "Tartart")
    print(band_name_generator('sandles'), "Sandlesandles")
    print(band_name_generator('bed'), 'The Bed')
    print(band_name_generator('qq'), "Qqq")