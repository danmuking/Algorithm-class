import os.path as osp
import os
import datetime
'''
@author: 林逸
@software: PyCharm
@file: 1.py
@desc: 
@time: 2020/9/9 10:32
'''
def getInOUt(path):
    inners = []
    inPath = osp.join(path,"TEST")
    inFilePaths = os.listdir(inPath)
    for i in range(len(inFilePaths)):
        inFilePaths[i] = osp.join(inPath,inFilePaths[i])
        with open(inFilePaths[i],'r') as f:
            temp = f.readlines()
            for j in range(len(temp)):
                temp[j] = int(temp[j].strip())
            inners.append(temp)

     #print(inner)

    outers = []
    outPath = osp.join(path, "ANSWER")
    outFilePaths = os.listdir(outPath)
    for i in range(len(outFilePaths)):
        outFilePaths[i] = osp.join(outPath, outFilePaths[i])
        with open(outFilePaths[i],'r') as f:
            temp = f.readlines()
            for j in range(len(temp)):
                temp[j] = int(temp[j].strip())
            outers.append(temp)

    # print(outer)
    return inners,outers

def counting(inner):
    # print(inner[0])
    out = [0 for x in range(10)]
    for i in range(1,inner[0]+1):
        temp = i
        while(temp>0):
            out[temp%10] = out[temp%10]+1
            temp = temp//10
    return out

def checkResult(out,outer):
    if(out == outer):
        return True
    else:
        return False

if __name__ == '__main__':
    path = r"G:\Code\Algorithm class\1\1\COUNTING"
    inners,outers=getInOUt(path)
    for i in range(len(inners)):
        startTime = datetime.datetime.now()
        inner = inners[i]
        outer = outers[i]
        out = counting(inner)
        endTime = datetime.datetime.now()

        print("程序输入：", inner)
        print("程序输出：",out)
        print("正确输出：",outer)

        if(checkResult(out,outer)):
            print("正确")
        else:
            print("错误")
        print("运行时间：",endTime-startTime)
        print('-'*30)