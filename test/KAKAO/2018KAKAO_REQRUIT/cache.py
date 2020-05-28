#understanding & plan : 10min 50s
#coding : 18m 41
#total : 29m 31s

def solution(cacheSize, cities):
    t = 0
    stack = []
    for str in cities:
        if str.upper() in stack:
            stack.remove(str.upper())
            stack.append(str.upper())
            t+= 1
        else:
            t += 5
            stack.append(str.upper())
            if len(stack) > cacheSize:
                stack.pop(0)
        print(stack)
    return t

cs = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cs = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cs,cities))