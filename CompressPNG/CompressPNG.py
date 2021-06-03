# ----------------------------------------------------------------
#   File        ：CompressPNG\CompressPNG.py
#   Author      ：www.loywong.com
#   COPYRIGHT   ：(C)
#   Date        ：2019/06/16
#   Description ：批处理压缩Png贴图体积，方便集成到程序打包流程中
#   Version     ：1.0
#   Maintain    ：//[date] desc
# ----------------------------------------------------------------

import os,sys

# 不管何种执行方式，rootdir都是指当前python脚本所在目录
rootdir=sys.path[0]
# print(rootdir)

# 路径合成
# print(os.path.join(rootdir,'backup'))

# TEST os.system / os.startfile exec exe file --------------------------------------------- begin
# os.system("pngquant.exe")
# os.system(os.path.join(rootdir,'pngquant.exe')) -- 能获得帮助！！！
# os.startfile(os.path.join(rootdir,'pngquant.exe'))

# print(os.system(os.path.join(rootdir,'s2.png'))) -- 0
# print(os.startfile(os.path.join(rootdir,'s2.png'))) -- None
# print(os.startfile(os.path.join(rootdir,'backup')))
# TEST os.system / os.startfile exec exe file --------------------------------------------- end


#需要过滤的文件
notActionFile = ['test1_backup.png']
#需要过滤的文件夹
notActionPath = ['backup']
#需要删除的文件
needDeleteFile = ['test2.jpg']

# 取文件的扩展名
def file_extension(path): 
    return os.path.splitext(path)[-1] 

for (parent, dirnames, filenames) in os.walk(rootdir):
    print(dirnames) # 只是用来列举当前遍历到的目录的第一级子目录文件夹

    for filename in filenames:
        fullPath = os.path.join(parent,filename)
        print('filename: ' + fullPath)
        
        hasOP = False

        # 过滤文件夹
        lastPath = fullPath.split('\\')[-2]
        for onePath in notActionPath:
            if lastPath == onePath:
                print('过滤文件夹 lastPath___ ' + lastPath)
                hasOP = True
                break
                
        if hasOP is True:
            continue

        # 删除文件
        for deleteFile in needDeleteFile:
            if filename == deleteFile:      
                os.remove(fullPath)
                print('删除文件 filename___ ' + fullPath)
                hasOP = True
                break
        
        if hasOP is True:
            continue

        # 过滤文件
        for noActionName in notActionFile:  
            if noActionName == filename:
                print('过滤文件 filename___ ' + fullPath)
                hasOP = True
                break
        
        if hasOP is True:
            continue

        print('file_extension: ' + file_extension(fullPath))
        if file_extension(fullPath) == ".png":
            os.system(os.path.join(rootdir,'pngquant.exe') + " -f --ext .png --quality 50-80 \"" + fullPath  + "\"")
            print('___png___ ' + fullPath)

os.system('pause & exit')