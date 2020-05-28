import os
import datetime

metaFiles = ['main.py']
fExtensions = ['.py','.cpp']
seperator = ''.join(['-']*30)

def write(f_name,f_write):
    f_read = open(f_name,"r")
    comments = []
    lines = f_read.read().split('\n')
    modifiedTime = os.path.getmtime(f_name) 
    
    for line in lines:
        if '#' in line:
            comment = line.replace('#','')+'\n'
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
            if os.path.splitext(entry)[-1] not in fExtensions or entry in metaFiles:
                continue
            write(path,f_write)
            
def main():
    f_write = open("result.txt","w")
    basePath = './'
    writeFilesRecursively(basePath,f_write)
    f_write.close()

main()
