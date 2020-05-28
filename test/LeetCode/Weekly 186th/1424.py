def findDiagonalOrder(nums):
    diagonals = {}
    for i, line in enumerate(nums):
        for j in range(len(line)):
            if i+j not in diagonals.keys():
                diagonals[i+j] = []
            diagonals[i+j].append(line[j])
    ret = []
    for i in range(len(diagonals)):
        ret.extend(diagonals[i][::-1])
    return ret

#print(findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
#print(findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
#print(findDiagonalOrder([[3,3,18],[4,15,11],[19,11,14,14,3]]))
print(findDiagonalOrder([[1],[2],[3]]))