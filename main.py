import os
import datetime

metaFiles = ['main.py']
fExtensions = ['.py','.cpp']
commentType = {'.py':'#','.cpp':'//'}
seperator = ''.join(['-']*30)
noOfSolved = 0

def write(f_name,f_write,f_extension):
    global noOfSolved
    noOfSolved += 1
    f_read = open(f_name,"r")
    comments = []
    lines = f_read.read().split('\n')
    modifiedTime = os.path.getmtime(f_name) 
    commentSymbol = commentType[f_extension]
    for line in lines:
        if commentSymbol in line:
            comment = line.replace(commentSymbol,'')+'\n'
            comments.append(comment)
    
    if len(comments) > 0:
        f_write.write(seperator+'\n')
        value = datetime.datetime.fromtimestamp(modifiedTime)
        f_write.write(f"{value:%Y-%m-%d %a %H:%M:%S}"+'\n')
        f_write.write(f_name+'\n')
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
            
def main():
    f_write = open("result.txt","w")
    basePath = './'
    writeFilesRecursively(basePath,f_write)
    f_write.write('푼문제수 : {}'.format(noOfSolved))
    f_write.close()

main()
