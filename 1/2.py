import os.path as osp
import os
import datetime
import string

'''
@author: 林逸
@software: PyCharm
@file: 2.py
@desc: 
@time: 2020/9/9 11:50
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
                temp[j] = temp[j].strip()
            inners.append(temp)

    print(inners)

    outers = []
    outPath = osp.join(path, "ANSWER")
    outFilePaths = os.listdir(outPath)
    for i in range(len(outFilePaths)):
        outFilePaths[i] = osp.join(outPath, outFilePaths[i])
        with open(outFilePaths[i],'r') as f:
            temp = f.readlines()[:10]
            for j in range(len(temp)):
                temp[j] = int(temp[j].strip())
            outers.append(temp)

    print(outers)
    return inners,outers

def countBefore(m,n):
    temp1 = 1
    temp2 = 1
    for i in range(1,m+1):
        temp1 = temp1*i
    for i in range(n-m+1,n+1):
        temp2 = temp2*i
    return int(temp2/temp1)

def dictionary(inner):
    out = []
    eachNums = inner[1:]
    for eachNum in eachNums:
        # eachNum = "ahou"
        # print(eachNum)
        sum = 0
        for i in range(1,len(eachNum)):
            sum = sum + countBefore(i,26)
        # print(sum)
        for i in range(len(eachNum) - 1):
            if(i == 0):
                temp = ord(eachNum[i]) - 97
            else:
                temp = ord(eachNum[i]) - ord(eachNum[i-1]) - 1
            for j in range(temp):
                if i==0:
                    n = 26 - j - 1
                else:
                    n = 26 - (ord(eachNum[i-1]) - 96) - j - 1
                m = len(eachNum) - i - 1;
                sum = sum + countBefore(m,n)
                # print(m,n)
        # print(sum)
        if len(eachNum) == 1:
            sum = sum + ord(eachNum[0]) - 96
        else:
            sum = sum + ord(eachNum[-1]) - ord(eachNum[-2])
        out.append(sum)
    return out

def checkResult(out,outer):
    if(out == outer):
        return True
    else:
        return False



if __name__ == '__main__':
    path = r"G:\Code\Algorithm class\1\1\DICTIONARY"
    inners,outers = getInOUt(path)
    for i in range(len(inners)):
        startTime = datetime.datetime.now()
        inner = inners[i]
        outer = outers[i]
        out = dictionary(inner)
        endTime = datetime.datetime.now()

        print("程序输入：", inner)
        print("程序输出：", out)
        print("正确输出：", outer)

        if (checkResult(out, outer)):
            print("正确")
        else:
            print("错误")
        print("运行时间：", endTime - startTime)
        print('-' * 30)