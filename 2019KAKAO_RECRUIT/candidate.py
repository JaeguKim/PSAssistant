#planning : 13m 52
from itertools import combinations

def solution(relation):
    answer = 0
    all = []
    uniqueIdx = []

    if len(relation) > 0:
        colSize = len(relation[0])
        rowSize = len(relation)

        for i in range(1,colSize+1):
            all.extend([set(k) for k in combinations([j for j in range(colSize)],i)])
            print(all)
        for comb in all:
            validSet = set()
            for row in range(rowSize):
                temp = ''
                for col in comb:
                    temp += relation[row][col]
                validSet.add(temp)
            if len(validSet) == rowSize:
                uniqueIdx.append(comb)
        
        delSet = set()
        for stdMinElem in uniqueIdx:
            for idx,compMinElem in enumerate(uniqueIdx):
                if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                    delSet.add(uniqueIdx.index(compMinElem))
        answer = len(uniqueIdx) - len(delSet)
        return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))