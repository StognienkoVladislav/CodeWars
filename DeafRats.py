
def count_deaf_rats(town):
    
    right = "~O"
    left  = "O~"

    town = town.replace(right,"R")
    town = town.replace(left, "L")

    for x in town:
        if x == 'P':
            piper = town.index(x)

    count = 0
    print(town)
    
    for x in town:
        ind = town.index(x)
        if ind > piper and x == "R":
            count += 1
        elif ind < piper and x == "L":
            count += 1    
        else:
            pass
    return count

if __name__ == '__main__':
    print(count_deaf_rats("~O~O~O~O P"), 0)
    print(count_deaf_rats("P O~ O~ ~O O~"), 1)
    print(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)