#!/Users/pinpip/miniconda3/bin/python

# Quick-Union, Algo: Quick-Find, Initialize: O(N)
#           , Union: O(N) "faster than Quick-Find", Find: O(N).
#           , For N union operations: O(N^2) 
# Tree aproach
# Trees can get tall.
# Improvement, tree weight balancing.
# Nodes from 0 to Size(excluded)
def main():
    size = 10
    # qf_list = fill_list(size)
    random_list = [0, 1, 9, 4, 9, 6, 6, 7, 8, 9]
    print(get_parent(random_list, 1))
    union(random_list, 0, 1)
    print(random_list)
    union_weighed(random_list, 0, 3)
    print(random_list)

def detect_cycle(list_):
    pass #TODO: Implement cycle detection

def connected(list_, p, q):
    return get_parent(list_, p) == get_parent(list_, q)

def get_parent(list_, p):
    i = p
    while list_[i] != i:
        i = list_[i]
    return i

def union(list_, p, q):
    i = get_parent(list_, p)
    j = get_parent(list_, q)
    list_[i] = j
    
#Improvement
def get_weight(list_, p):
    counter = 1
    i = p
    while list_[i] != i:
        i = list_[i]
        counter += 1
    return counter

def union_weighed(list_, p, q):
    p_weight = get_weight(list_, p)
    q_weight = get_weight(list_, q)
    print(f"P weight: {p_weight}, Q weight: {q_weight}")
    if p_weight > q_weight:
        union(list_, q, p)
    else:
        union(list_, p, q)

def fill_list(n):
    return [x for x in range(n)]

if __name__ == "__main__":
    main()