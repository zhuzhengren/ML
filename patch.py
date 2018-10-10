import os,time, re, shutil
env_dist=os.environ;

#bakpath=env_dist.get('backpath')
#bakpath='/home/gjb/'+bakpath;
#baktime=env_dist.get('baktime');
frompath="/var/lib/jenkins/workspace/Howto_Patch_Build/app/build/outputs/apk/"
bakpath ='C:\\Users\\zhuzhengren\\Desktop\\51\\orgin\\'

buildtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
topath=bakpath+"..\..\\"+buildtime;

#拷贝原始文件
names = os.listdir(frompath)
for name in names:
    if re.match(r'.*.apk', name):
        print(name)
        if not os.path.exists(topath + "orgin\\"):
            os.makedirs(topath + "orgin\\")
        shutil.copy(frompath+ name, topath + "orgin\\")

patchpath= frompath+"patch/howto/release/patch_signed_7zip.apk"
os.makedirs(topath + "patch\\")
shutil.copy(frompath+ name, topath + "patch\\")


