def solution(N, stages):
    hash = []
    failRate = {}
    for i in range(N+1):
        hash.append(0)
        failRate[i+1] = 0.0

    for stage in stages:
        hash[stage-1] += 1
    sum = 0
    for i in range(N):
        if i == N-1:
            if hash[i] != 0 and hash[i+1] != 0:
                failRate[i+1] = hash[i]/(hash[i]+hash[i+1])
                break
        sum = hash[i]
        for j in range(i+1,N+1):
            sum+=hash[j]
        if sum == 0:
            failRate[i+1] = 0
        else:
            failRate[i+1] = hash[i]/sum
    answer =  [ v[0] for v in sorted(failRate.items(), key=lambda dictItem: dictItem[1],reverse=True)]
    return answer[:-1]