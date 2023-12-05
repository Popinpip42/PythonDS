#!/a/Anaconda/python

# Quick-Union, 
# 
# Nodes from 0 to Size(excluded)
def main():
    size = 10
    # qf_list = fill_list(size)
    random_list = [0, 1, 9, 4, 9, 6, 6, 7, 8, 9]
    print(get_parent(random_list, 8))

def get_parent(list, p):
    i = p
    while list[i] != i:
        i = list[i]
    return i

def connected(list, p, q):
    for i in range(len(list)):
        pass

def fill_list(n):
    return [x for x in range(n)]

if __name__ == "__main__":
    main()