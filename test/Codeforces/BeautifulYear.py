#6m 52s
year = int(input())
while True:
    year+=1
    hash = {}
    for ch in str(year):
        hash[ch] = 0
    if len(hash) == 4:
        print(year)
        break