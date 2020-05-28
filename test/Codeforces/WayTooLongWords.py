#14min
#more than = greater than
n = int(input())
for i in range(n):
    line = input()
    #print(len(line))
    if len(line) <= 10:
        print(line)
    else:
        res = [line[0],str(len(line)-2),line[-1]]
        print(''.join(res))
