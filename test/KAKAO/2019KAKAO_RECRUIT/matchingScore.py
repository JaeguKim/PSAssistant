import re

def solution(word, pages):
    res = {}
    for i in range(len(pages)):
        head = pages[i].split('<head>')[1].split('</head>')[0]
        url = head.split('<meta property=\"og:url\" content=\"')[1].split('\"')[0]
        #url = head.split('og:url')[1].split('content=\"')[1].split("\"")[0]
        body = pages[i].split('<body>')[1].split('</body')[0]
        links = []
        cnt = 0
        temp = pages[i]
        linkmeta = '<a href=\"'
        while linkmeta in temp:
            startIdx = temp.index(linkmeta)+len(linkmeta)
            endIdx = temp.index('\"',startIdx)
            links.append(temp[startIdx:endIdx])
            temp = temp[endIdx:]
        arr = re.split(r"[^A-Za-z]",body.lower())
        for item in arr:
            if item == word.lower():
                cnt+=1
        res[url] = [links,cnt,0,i]
    for key in res.keys():
        basicScore = res[key][1]
        lengthOfLinks = len(res[key][0])
        for link in res[key][0]:
            if link in res.keys():
                if lengthOfLinks != 0:
                    res[link][2] += basicScore/lengthOfLinks
        res[key][2] += basicScore
    answer = sorted(res.items(),key=lambda x:x[1][2],reverse=True)
    return answer[0][1][3]

#print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))