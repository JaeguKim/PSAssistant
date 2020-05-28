#수에 대한 감각이 필요한 문제같다
X = int(input())
for A in range(-198,200):
    for B in range(-119,119):
        if pow(A,5) - pow(B,5) == X:
            print('{} {}'.format(A,B))
            exit()