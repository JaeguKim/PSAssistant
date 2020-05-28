def check(result):
    for x,y,type in result:
        if type == 0:
            if y == 0 or (x-1,y,1) in result or (x,y,1) in result or (x,y-1,0) in result:
                continue
            else:
                return False
        elif type == 1:
            if (x,y-1,0) in result or (x+1,y-1,0) in result or ((x-1,y,1) in result and (x+1,y,1) in result):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result = set()
    answer = []
    for elem in build_frame:
        x,y,type,isAdd = elem
        if isAdd == 1:
            result.add((x,y,type))
            isTrue = check(result)
            if isTrue:
                continue
            else:
                result.remove((x,y,type))
        elif isAdd == 0:
            if (x,y,type) in result:
                result.remove((x,y,type))
                isTrue = check(result)
                if isTrue:
                    continue
                else:
                    result.add((x,y,type))
    
    result = [list(item) for item in result]
    answer = sorted(result,key= lambda x: (x[0],x[1],x[2]))
    
    return answer

#print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))