#!/a/Anaconda/python

# Union find, Algo: Quick-Find, Initialize: O(N)
#           , Union: O(N), Find: O(1).
#           , For N union operations: O(N^2) 
# Eage approach
# Nodes from 1 to Size
def main():
    size = 10
    uf_list = create_list(size + 1)
    print(uf_list)
    union(uf_list, 2, 10) #Connect 2 and 10
    union(uf_list, 2, 1) #Connect 2 and 1
    print(uf_list)
    print(find(uf_list, 2))
    print(connected(uf_list, 2, 10))

def detect_cycle(list):
    if 1 > 0:
        pass # TODO: implement cycle detection

def connected(list, n1, n2):
    return list[n1-1] == list[n2-1]

def find(list, n1):
    if 1 < n1 < len(list) + 1:
        return list[n1 - 1]
    return None

def union(list, n1, n2):
    n1_value = list[n1-1]
    n2_value =  list[n2-1]
    for i in range(len(list)):    
        if list[i] == n1_value:
            list[i] = n2_value

def create_list(end):
    return [x for x in range(1, end)]

if __name__ ==  "__main__":
    main()