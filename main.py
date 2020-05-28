import os

metaFiles = ['result.txt','main.py','.git']
seperator = ''.join(['-']*30)

def write(f_name,f_write):
    f_read = open(f_name,"r")
    print(f_name)
    lines = f_read.read().split('\n')
    f_write.write(seperator+'\n')
    f_write.write(f_name+'\n')
    for line in lines:
        if '#' in line:
            res = line.replace('#','')+'\n'
            f_write.write(res)
    f_write.write(seperator)
    f_read.close()

def getFileList():
    basePath = './'
    res = []
    for entry in os.listdir(basePath):
        if entry not in metaFiles:
            if os.path.isfile(os.path.join(basePath,entry)):
                res.append(entry)
    return res

def getDirectoryList():
    basePath = './'
    res = []
    for entry in os.listdir(basePath):
        if os.path.isdir(os.path.join(basePath,entry)):
            res.append(entry)
    return res

def writeFilesRecursively(basePath,f_write):
    #basePath = './'
    for entry in os.listdir(basePath):
        if entry in metaFiles:
            continue
        path = os.path.join(basePath,entry)
        if os.path.isdir(path):
            writeFilesRecursively(path,f_write)
        elif os.path.isfile(path):
            write(path,f_write)
            
def main():
    f_write = open("result.txt","w")
    # f_list = getFileList()
    # for f_name in f_list:
    #     write(f_name,f_write)
    basePath = './'
    writeFilesRecursively(basePath,f_write)
    f_write.close()

main()
#print(getDirectoryList())
