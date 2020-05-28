#문제의 요구조건을 수식으로 표현했을때 풀리는 문제 : j-i = Ai + Aj => i+Ai = j-Aj
n = int(input())
heights = [int(ch) for ch in input().split()]
ans = 0
dict = {}
for i in range(len(heights)):
    key = i+heights[i]
    if key in dict.keys():
        dict[key] += 1
    else:
        dict[key] = 1
for i in range(len(heights)):
    key = i-heights[i]
    if key in dict.keys():
        ans+=dict[key]
print(ans)

