import random
import time
from tqdm import tqdm

def generateNum(num):
    """
    生成随机数
    @param num: 生成随机数的数量
    @return: 包含所有随机数的列表
    """
    return [random.randint(-num*10,num*10) for i in range(num)]

def bubbleSort(arr):
    for i in tqdm(range(len(arr)-1)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    return arr

if __name__ == '__main__':
    numOfNum = [10,100,1000,100000]
    mode = 'bubble'
    print("排序算法:"+mode)
    for each in numOfNum:
        num = generateNum(each)
        start = time.time()
        if(mode == 'bubble'):
            result = bubbleSort(num)
        end = time.time()
        print("程序输入：",num)
        print("程序输出：",result)
        print("运行时间：",end-start,"s")
