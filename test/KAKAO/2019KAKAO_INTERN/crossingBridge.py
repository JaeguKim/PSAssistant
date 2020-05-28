#2hour
#python에서 int는 immutable타입이므로 함수 parameter로 전달하고 리턴되면 함수안에서 했던 작업들이 반영되지 않음
def check(stones,k,m):
    size = len(stones)
    cnt = 0
    for i in range(size):
        if (stones[i]-(m-1)) <= 0:
            cnt+=1
            if cnt == k:
                return False
        else:
            cnt = 0
    return True


def binarySearch(stones,left,right,k,res):
    if left > right:
        return
    mid = int((left+right)/2)
    if check(stones,k,mid):
        res[0] = max(res[0],mid)
        binarySearch(stones,mid+1,right,k,res)
    else:
        binarySearch(stones,left,mid-1,k,res)
    

def solution(stones, k):
    max = 200000000
    res = [0]
    binarySearch(stones,1,max,k,res)
    return res[0]
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))