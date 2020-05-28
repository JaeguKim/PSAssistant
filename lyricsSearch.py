#1hour 04min : 2018년 문제에서 배운지식으로 응용하여 풀수 있었다.
#TRIE로 구현
class Node():
    def __init__(self):
        self.next = {}
        self.cntDict = {}
        self.value = 0

def printNode(parent,key):
    print('{} {} {}'.format(key,parent.value,parent.cntDict))
    next = parent.next
    for key in next.keys():
        printNode(next[key],key)

def makeTrie(words):
    root = Node()
    for word in words:
        temp = root
        temp.value+=1
        for ch in word:
            if len(word) not in temp.cntDict.keys():
                temp.cntDict[len(word)] = 1
            else:
                temp.cntDict[len(word)] += 1
            if ch not in temp.next:
                temp.next[ch] = Node()
            temp.next[ch].value+=1
            temp = temp.next[ch]
    return root

def solution(words, queries):
    sortedWords = sorted(words)
    reversedWords = []
    for word in words:
        reversedWords.append(word[::-1])
    sortedReversed = sorted(reversedWords)
    root1 = makeTrie(sortedWords)
    root2 = makeTrie(sortedReversed)
    # printNode(root1,'parent')
    # print('==================')
    # printNode(root2,'parent')
    res = []
    for query in queries:
        cur = None
        if query[0] == '?':
            cur = root2
            query = query[::-1]
        else:
            cur = root1
        for ch in query:
            #print('ch : {} , value : {}'.format(ch,cur.value))
            if ch == '?':
                cnt = len(query)
                if cnt in cur.cntDict.keys():
                    res.append(cur.cntDict[cnt])
                else:
                    res.append(0)
                break
            elif ch not in cur.next.keys():
                res.append(0)
                break
            else:
                cur = cur.next[ch]
    return res

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))