def solution(board,moves):
    stack = []
    cnt = 0
    for elem in moves:
        for i in range(len(board)):
            if board[i][elem-1] != 0:
                if len(stack) != 0 and stack[-1] == board[i][elem-1]:
                    cnt+=2
                    stack.pop()
                else:
                    stack.append(board[i][elem-1])
                board[i][elem-1] = 0
                break
    return cnt
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))

                
