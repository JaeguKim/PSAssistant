#understanding : 3m 51s
#coding : 52m
#total : 55m 19s
def makeSet(str):
    emptySet = set()
    for i in range(len(str)-1):
        if str[i:i+2].isalpha():
            emptySet.add(str[i:i+2].upper())
    return emptySet

def makeList(str):
    list = []
    for i in range(len(str)-1):
        if str[i:i+2].isalpha():
            list.append(str[i:i+2].upper())
    return list

def solution(str1, str2):
    list1 = makeList(str1)
    list2 = makeList(str2)
    set1 = makeSet(str1)
    set2 = makeSet(str2)
    if len(list1) == 0 and len(list2) == 0:
        return 65536
    print(list1)
    print(list2)

    bunza = 0
    bunmo = 0
    union = set1.union(set2)
    print(union)
    inter = set1.intersection(set2)
    print(inter)
    for elem in union:
        bunmo += max(list1.count(elem),list2.count(elem))
    for elem in inter:
        bunza += min(list1.count(elem),list2.count(elem))

    return int((bunza/bunmo)*65536)


s1 = "aa1+aa2"
s2 = "AAAA12"
print(solution(s1,s2))
s1 = "handshake"
s2 = "shake hands"
print(solution(s1,s2))