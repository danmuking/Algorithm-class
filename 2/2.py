import random
import time
from tqdm import tqdm

def generateNum(num):
    """
    生成随机数
    @param num: 生成随机数的数量
    @return: 包含所有随机数的列表
    """
    return [random.randint((-num*10),(num*10)) for i in range(num)]

def bubbleSort(arr):
    """
    冒泡排序
    @param arr: 需要排序的数字列表
    @return: 排序完成的数字列表
    """
    for i in tqdm(range(len(arr)-1)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def selectionnSort(arr):
    '''
    选择排序
    @param arr: 需要排序的数字列表
    @return: 排序完成的数字列表
    '''
    for i in tqdm(range(len(arr))):
        minIndex = i
        for j in range(i,len(arr)):
            if(arr[j]<arr[minIndex]):
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr

def insertionSort(arr):
    '''
    选择排序
    @param arr: 需要排序的数字列表
    @return: 排序完成的数字列表
    '''
    emptyList = [arr[0]]
    for i in range(1,len(arr)):
        if (arr[i] <= emptyList[0]):
            emptyList.insert(0, arr[i])
        elif (arr[i] >= emptyList[-1]):
            emptyList.append(arr[i])
        else:
            for j in range(len(emptyList)-1):
                if(emptyList[j]<=arr[i] and emptyList[j+1]>=arr[i]):
                    emptyList.insert(j+1,arr[i])
                    break
    return emptyList

def quickSort(arr,left,right):
    """
    快速排序
    @param arr: 需要排序的数组
    @param left: 排序的起始位置
    @param right: 排序的结束位置
    @return: 排好序的数组
    """
    if(left<right):
        markIndex = miniFunc(arr,left,right)
        # 使用递归进行分治，将Mark值的左右分别排序
        quickSort(arr,left,markIndex-1)
        quickSort(arr,markIndex+1,right)
    return arr

def miniFunc(arr,left,right):
    """
    将数组大于mark的值移到makr左边，小于mark的值移到mark右边
    @param arr: 需要排序的数组
    @param left: 排序的起始位置
    @param right: 排序的结束位置
    @return: mark的位置
    """
    mark = left
    start = mark
    end = right
    while start<end:
        # 注意一下等于的条件
        while arr[end]>=arr[mark] and start<end:
            end = end-1
        while arr[start]<=arr[mark] and start<end:
            start = start+1

        arr[start],arr[end] = arr[end],arr[start]
    arr[mark],arr[end]=arr[end],arr[mark]
    return end


def heap(arr,n,i):
    """
    构造大根堆
    @param arr: 需要排序的数组
    @param n: 需要排序数的个数
    @param i: 当前所在非叶节点位置
    """
    largest = i
    #叶节点的左节点
    l = 2*i+1
    #叶节点的右节点
    r = 2*i+2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr,n,largest)

def heapSort(arr):
    """
    堆排序
    @param arr: 需要排序的数组
    @return: 完成排序的数组
    """
    n = len(arr)
    #从最后一个非叶节点开始
    for i in range(n,-1,-1):
        #构造大根堆
        heap(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heap(arr,i,0)
    return arr



if __name__ == '__main__':
    numOfNum = [5,100,1000,100000]
    mode = 'bubble'
    print("排序算法:"+mode)
    for each in numOfNum:
        num = generateNum(each)
        # num = [-6, 47, 7]
        checkList = num.copy()
        checkList.sort()
        start = time.time()
        if(mode == 'bubble'):
            result = bubbleSort(num)
        elif(mode == "selection"):
            result = selectionnSort(num)
        elif(mode == 'insertion'):
            result = insertionSort(num)
        elif(mode == "quick"):
            result = quickSort(num,0,len(num)-1)
        elif(mode == "heap"):
            result = heapSort(num)
        end = time.time()
        if(result==checkList):
            print("列表长度为{},排序正确".format(len(num)))
        print("运行时间：",end-start,"s")