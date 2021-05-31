# ----------------------------------------------------------------
#   File        ：CreateResourceConfig\CreateResourceConfig.py
#   Author      ：www.loywong.com
#   COPYRIGHT   ：(C)
#   Date        ：2019/04/16
#   Description ：涉及对系统目录及文件的操作
#               示例：为CocosCreater项目创建.ts代码类型的资源配置文件
#   Version     ：1.0
#   Maintain    ：//[date] desc
# ----------------------------------------------------------------

# 导入标准库os
import os

# !!! 请先确认路径是否正确 !!!
# 1 如果在VSCode的运行环境中，输出当前vs工程所在目录（注意不是指当前py脚本文件所在具体目录）
# 2 如果脚本使用系统默认py.exe执行，则输出的是当前py脚本所在的系统目录
print("Current Project Path: " + os.getcwd())

# 定义资源文件所在目录
assetsPath = os.getcwd() + "/Assets"

# 定义配置文件生成的目录
# !!!由于本脚本没有提供动态创建文件夹的方法，所以请预创建好目标文件夹 /Config
outFile = os.getcwd() + "/Config/AssetsConfig.ts"

# 优先需要排除的文件类型
preExcludeCategorys = [".meta"]
# 包含的文件类型（根据工程需要写入）
includeCategorys = [".png", ".jpg", ".mp3", ".wav", ".prefab", ".anim"]

# 缓存所有资源的目录值
lines = []

def collectAssetsPath():
    print("Read Assets Name And Path ------------ Start!")
    
    # 开始遍历工程目录，按文件夹层级递归
    # Path：所有文件夹目录
    # dirs：文件夹下的所有子文件夹
    # files：文件夹下的所有文件
    for (path, dirs, files) in os.walk(assetsPath):
        print("Folder: " + path)
        # print(dirs)
        # print(files)
        # print("Folder's Files Count: " + str(len(files)))

        # 判断是否为空文件夹
        if len(files) == 0:
            print("Folder Is Empty!!!")
            continue

        for filename in files:
            # 优先判断：需要排除所有的meta文件
            isPreExclude = False
            for c in preExcludeCategorys:
                if filename.find(c) != -1:
                    isPreExclude = True
                    break
            # 如果是需要排除的文件，则跳过
            if isPreExclude is True:
                continue
            
            # 文件名称
            resName = ""
            for c in includeCategorys:
                if filename.find(c) != -1:
                    nameArr = filename.split(".")
                    resName = nameArr[0]
                    break
            
            # 如果文件名称非法，则跳过
            if resName == "":
                continue

            # 否则开始格式化需要的内容形式 line
            # 根目录Assets不需要记录，优化字节数
            startIndex = path.index("Assets") + len('Assets') + 1
            resPath = path[startIndex:]
            resPath = resPath.replace("\\", "/")
            resPath = resPath + "/" + resName
            line = "\t" + resName + " : \"" + resPath + "\",\n"
            print("Valid Config: " + line)

            # 重复资源判断
            if line in lines:
                print("Read Name And Path Error!, res name repeat!  >>>" + resName)
                return False

            lines.append(line)

    print("Read Assets Name And Path ------------ Success!")
    return True

# 往资源配置文件写入数据
def writeFile():
    print("Write Config File ------------ Start!")
    dst = open(outFile, 'w', encoding='utf-8')
    dst.write("export let AssetsConfig = {\n")
    for line in lines:
        dst.write(line)
        print(line)
    dst.write("}")
    print("Write Config File ------------ Success!")
    dst.close()

######################################################################
# 定义完成，开始逻辑执行
isOk = collectAssetsPath()
# print(lines)
if isOk:
    # 排序（实际效果：按照资源的命名）
    lines.sort()
    writeFile()
    
os.system('pause & exit')