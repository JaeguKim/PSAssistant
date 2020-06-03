import os
import datetime

metaFiles = ['main.py']
fExtensions = ['.py','.cpp']
commentType = {'.py':'#','.cpp':'//'}
seperator = ''.join(['-']*30)
totalSolved = 0
noOfSolved = {'.py':0, '.cpp':0}
newline = '\n'

def printNewLine(f_write):
    f_write.write(newline)

def write(f_name,f_write,f_extension):
    global noOfSolved
    global totalSolved
    totalSolved += 1
    noOfSolved[f_extension] += 1
    f_read = open(f_name,"r")
    comments = []
    lines = f_read.read().split(newline)
    modifiedTime = os.path.getmtime(f_name) 
    commentSymbol = commentType[f_extension]
    for line in lines:
        if commentSymbol in line:
            comment = line.replace(commentSymbol,'')+newline
            comments.append(comment)
    
    if len(comments) > 0:
        f_write.write(seperator)
        printNewLine(f_write)
        value = datetime.datetime.fromtimestamp(modifiedTime)
        f_write.write(f"{value:%Y-%m-%d %a %H:%M:%S}"+newline)
        f_write.write(f_name+newline)
        for comment in comments:
            f_write.write(comment)
        f_write.write(seperator)
        f_read.close()

def writeFilesRecursively(basePath,f_write):
    #basePath = './'
    for entry in os.listdir(basePath):
        path = os.path.join(basePath,entry)
        if os.path.isdir(path):
            writeFilesRecursively(path,f_write)
        elif os.path.isfile(path):
            f_Extension = os.path.splitext(entry)[-1]
            if f_Extension not in fExtensions or entry in metaFiles:
                continue
            write(path,f_write,f_Extension)

def printMetric(f_write):
    printNewLine(f_write)
    f_write.write('총 푼문제수 : {}'.format(totalSolved))
    printNewLine(f_write)
    f_write.write('C++로 푼 문제수 : {}'.format(noOfSolved['.cpp']))
    printNewLine(f_write)
    f_write.write('Python으로 푼문제수 : {}'.format(noOfSolved['.py']))
    printNewLine(f_write)

def main():
    f_write = open("result.txt","w")
    basePath = './'
    writeFilesRecursively(basePath,f_write)
    printMetric(f_write)
    f_write.close()

main()
