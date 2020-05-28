#22min
n = int(input())
list = map(int,input().split())
pair = []
for idx,num in enumerate(list):
    pair.append([idx+1,num])
pair = sorted(pair,key=lambda x:x[1])
for item in pair:
    print(item[0],end=' ')
