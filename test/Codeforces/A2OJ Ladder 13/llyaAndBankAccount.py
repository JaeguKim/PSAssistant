#25min
n = input()
removeLast = int(''.join((n[:len(n)-1])))
str = ''.join(n[:len(n)-2]) + n[-1]
removeBeforeLast = int(str)
print(max(max(int(n),removeLast),removeBeforeLast))
