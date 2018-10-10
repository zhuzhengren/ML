import sys,re,os,shutil,time
is_publish= sys.argv[1]
channels=sys.argv[2]
#frompath="/var/lib/jenkins/workspace/Howto_ReleaseBuild/app/build/outputs/apk/"
frompath="C:\\Users\\zhuzhengren\\Desktop\\51\\"
#basepath="/home/gjb/data/build_res/hotfix/howto/release_hotifx_build/"
basepath='d:\\'
choosebranch="origin/release/1.1.10-百度"
version = re.match(r'(.*)\/(.*)', choosebranch).group(2)
buildtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
BUILD_NUMBER='18'
is_publish="true"
channels="baidu,anzhi,tencent"
channels=''
if is_publish=='truea':
    #正式发版拷贝的路径
    topath=basepath+version+"\\"+buildtime+'\\';
else:
    # 非正式发版拷贝的路径
    topath = basepath+BUILD_NUMBER;

if channels=='':
    print("拷贝全部文件")
    shutil.copytree(frompath,topath)
else:
   # 先拷贝未加固的原始包
    if not os.path.exists(topath + "\\orgin\\"):
        os.makedirs(topath + "\\orgin\\")
    names = os.listdir(frompath)
    for name in names:
        if re.match(r'.*.apk', name):
            shutil.copy(frompath + name, topath + "\\orgin\\")
    print("拷贝指定文件")
    channels=channels.split(',')
    for channel in channels:
       if channel=='tencent':
           print("拷贝腾讯包")
           names = os.listdir(frompath + "tencentjiagu")
           for name in names:
                if re.match(r'.*_'+channel+'.apk',name):
                    print(name)
                    if not os.path.exists(topath+"\\jiagu\\tencent\\"):
                        os.makedirs(topath+"\\jiagu\\tencent\\")
                    shutil.copy(frompath+"tencentjiagu\\"+name,topath+"\\jiagu\\tencent\\")
       else:
           print("拷贝360加固包")
           names = os.listdir(frompath + "360jiagu")
           for name in names:
                if re.match(r'.*_'+channel+'.apk',name):
                    print(name)
                    if not os.path.exists(topath+"\\jiagu\\360jiagu\\"):
                        os.makedirs(topath+"\\jiagu\\360jiagu\\")
                    shutil.copy(frompath+"360jiagu\\"+name,topath+"\\jiagu\\360jiagu\\")
