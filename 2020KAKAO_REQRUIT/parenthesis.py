def isBalanced(str):
    num = 0
    for idx,value in enumerate(str):
        if value == '(':
            num+=1
        elif value == ')':
            num-=1
        if num == 0:
            return idx

def isRight(str):
    stack = []
    for ch in str:
        if len(stack)>0 and ch == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(ch)
    return (len(stack) == 0)

def solution(p):
    if p == "" or isRight(p): return p
    u,v = p[:isBalanced(p)+1],p[isBalanced(p)+1:]
    if isRight(u):
        string = solution(v)
        return u+string
    else:
        temp = '(' + solution(v) + ')'
    u = list(u[1:-1])
    for i in range(len(u)):
        if u[i] == '(':
            u[i] = ')'
        else:
            u[i] = '('
    return temp + "".join(u)