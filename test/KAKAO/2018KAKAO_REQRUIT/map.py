#understanding : 3min
#coding : 27min 
#total : 30min
import collections
def convertToList(num,n):
    queue = collections.deque()
    while num >= 2:
        remainder = num%2
        num = int(num/2)
        queue.appendleft(remainder)
    queue.appendleft(num)
    for i in range(n-len(queue)):
        queue.appendleft(0)
    return list(queue)

def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    map3 = []
    for i in range(n):
        map1.append(convertToList(arr1[i],n))
        map2.append(convertToList(arr2[i],n))
    for i in range(n):
        str = ''
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                str+='#'
            elif map1[i][j] == 0 and map2[i][j] == 0:
                str+=' '
        map3.append(str)
    print(map3)
    return map3

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

n=5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
solution(n,arr1,arr2)
solution2(n,arr1,arr2)
