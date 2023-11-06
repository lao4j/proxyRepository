import os,time,shutil
from os import system

def copyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exit!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile, dstfile)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
day = time.strftime('%d', now)
dayDir = '/usr/local/git_repository/pub/data/{}_{}_{}'.format(year, month, day)
listdir = os.listdir(dayDir)
listdir.sort(key=lambda x:os.path.getctime(dayDir +'/'+x))
isss = False
isclash = False
filenum = len(listdir)
for index in range(filenum):
    file = listdir[filenum - 1 - index]
    filesize = os.path.getsize(dayDir +'/'+file);
    if file.endswith('yaml') and not isclash:
        srcfile = '{}/{}'.format(dayDir, file)
        copyfile(srcfile, r"/usr/local/git_repository/proxyRepository/clash/clash.yaml")
        copyfile(srcfile, r"/usr/local/nginx/download/clash.yaml")
        isclash = True
    if file.endswith('txt') and not isss and filesize > 10000:
        srcfile = '{}/{}'.format(dayDir, file)
        copyfile(srcfile, r"/usr/local/git_repository/proxyRepository/ss/ss.txt")
        copyfile(srcfile, r"/usr/local/nginx/download/ss.txt")
        isss = True
system("sh /usr/local/git_repository/proxyRepository/forcepush.sh")

