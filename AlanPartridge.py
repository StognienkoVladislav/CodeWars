
def alan(arr):

    n = ['Rejection', 'Disappointment',
         'Backstabbing Central', 'Shattered Dreams Parkway']
    k = 0
    for x in n:
        for y in arr:
            if x == y:
                k += 1
                break

    if k == n.__len__():
        return 'Smell my cheese you mother!'

    else:
        return "No, seriously, run. You will miss it."


if __name__ == '__main__':
    print(alan(["Norwich", "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway", "London"]),
        "Smell my cheese you mother!")
    print(alan(["London", "Norwich"]), "No, seriously, run. You will miss it.")
    print(alan(["Norwich", "Tooting", "Bank", "Rejection", "Disappointment", "Backstabbing Central", "Exeter",
         "Shattered Dreams Parkway", "Belgium", "London"]), "Smell my cheese you mother!")
    print(alan(["London", "Norwich"]), "No, seriously, run. You will miss it.")
    print(alan(["London", "Shattered Dreams Parkway", "Backstabbing Central", "Disappointment", "Rejection", "Norwich"]),
        "Smell my cheese you mother!")