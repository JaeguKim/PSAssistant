#understanding : 11min
#coding : 33min
#total : 45min
import re

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    answer = sum(dart)
    return answer

def solution(dartResult):
    stack = []
    isContinue = False
    for i in range(len(dartResult)):
        if isContinue :
            isContinue = False
            continue
        if dartResult[i].isnumeric():
            if i+1 < len(dartResult) and dartResult[i+1].isnumeric(): 
                stack.append(int(dartResult[i:i+2]))
                isContinue = True
            else:
                stack.append(int(dartResult[i]))
        elif dartResult[i] == 'D':
            stack[-1] = pow(stack[-1],2)
        elif dartResult[i] == 'T':
            stack[-1] = pow(stack[-1],3)
        elif dartResult[i] == '*':
            if len(stack) > 1:
                stack[-1] *= 2
                stack[-2] *= 2
            elif len(stack) == 1:
                stack[-1] *= 2
        elif dartResult[i] == '#':
            stack[-1] *= -1
    return sum(stack)

dartResult = '1D2S#10S'
print(solution(dartResult))