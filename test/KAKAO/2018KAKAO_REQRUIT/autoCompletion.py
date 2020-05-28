#TRIE로 구현
class Node():
    def __init__(self):
        self.next = {}
        self.value = 0

def printNode(parent,key):
    print('{} {}'.format(key,parent.value))
    next = parent.next
    for key in next.keys():
        printNode(next[key],key)

def solution(words):
    root = Node()
    for word in words:
        temp = root
        temp.value+=1
        for ch in word:
            if ch not in temp.next:
                temp.next[ch] = Node()
            temp.next[ch].value+=1
            temp = temp.next[ch]
    res = 0
    for word in words:
        temp = root
        cnt = 0
        for idx,ch in enumerate(word):
            if temp.value == 1:
                break
            if idx == len(word)-1:
                cnt+=1
                break
            else:
                cnt+=1
                temp = temp.next[ch]
                #print('ch : {} , else block : {}'.format(ch,temp.value))
            #print('{} {}'.format(ch,cnt))
        res+=cnt
    return res

def compare3(word1, target, word2):
    for i in range(1, len(target)+1):
        if i == (len(target)) :
            return len(target)
        if (target[0:i] != word1[0:i]) and (target[0:i] != word2[0:i]):
            return i
        
def compare2(word1, target):
    for i in range(1, len(target)+1):
        if i == (len(target)) :
            return len(target)
        if target[0:i] != word1[0:i]:
            return i  
 
 #정렬후 양쪽비교 하는 방식으로 구현한 알고리즘
def solution2(words):
    answer = 0
    words.sort()
    for idx, word in enumerate(words):
        if idx == 0:
            answer += compare2(words[idx+1], words[idx])
        elif idx == (len(words)-1):
            answer += compare2(words[idx-1], words[idx])
        else:
            answer += compare3(words[idx-1], words[idx], words[idx+1])
    return answer

print(solution(["go", "gone", "guild"]))
#print(solution(["abc", "def", "ghi", "jklm"]))
#print(solution(["word", "war", "warrior", "world"]))

