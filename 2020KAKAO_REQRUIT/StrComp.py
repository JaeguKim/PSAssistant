def solution(s):
    length = len(s)
    answer = length
    for i in range(1,int(length/2)+1):
        count = 1
        result = ""
        temp = s[0:i]
        for j in range(i,length+1,i):
            subStr = s[j:j+i]
            print('subStr:  '+subStr)
            if temp == subStr:
                count+=1
            else:
                if count == 1:
                    result += temp
                else:
                    result += str(count) + temp
                    count = 1
                temp = subStr
        if length / i != 0:
            result += s[int(length/i)*i:]
        if answer > len(result):
            answer = len(result)
        print(result)
    return answer
                
print(solution("aabbaccc"))