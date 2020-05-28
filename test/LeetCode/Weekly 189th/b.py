class Solution:
    def arrangeWords(self, text: str) -> str:
        wordAry = text.split()
        wordList = []
        for i in range(len(wordAry)):
            word = []
            for ch in wordAry[i]:
                word.append(ch)
            wordList.append(word)
        for i in range(len(wordList)):
            wordList[i][0]=wordList[i][0].lower()
        sortAry = sorted(wordList,key=lambda x:len(x))
        res = ''
        sortAry[0][0] = sortAry[0][0].upper()
        for word in sortAry:
            for ch in word:
                res+=ch
            res+=' '
        return res.rstrip(' ')
