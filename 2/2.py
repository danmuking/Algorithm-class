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
    for i in tqdm(range(len(arr))):
        minIndex = i
        for j in range(i,len(arr)):
            if(arr[j]<arr[minIndex]):
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr

def insertionSort(arr):
    emptyList = [arr[0]]
    for i in tqdm(range(1,len(arr))):
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
    if(left<right):
        markIndex = miniFunc(arr,left,right)
        quickSort(arr,left,markIndex-1)
        quickSort(arr,markIndex+1,right)
    return arr

def miniFunc(arr,left,right):
    mark = left
    start = mark+1
    end = right
    while start<end:
        # 注意一下等于的条件
        while arr[end]>=arr[mark] and start<end:
            end = end-1
        while arr[start]<=arr[mark] and start<end:
            start = start+1
        arr[start],arr[end] = arr[end],arr[start]
    # if(arr[mark]>arr[start]):
    arr[mark],arr[end]=arr[end],arr[mark]
    return end
    # else:
    #     return mark

# def quickSort(arr, left=None, right=None):
#     left = 0 if not isinstance(left,(int, float)) else left
#     right = len(arr)-1 if not isinstance(right,(int, float)) else right
#     if left < right:
#         partitionIndex = partition(arr, left, right)
#         quickSort(arr, left, partitionIndex-1)
#         quickSort(arr, partitionIndex+1, right)
#     return arr
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot+1
#     i = index
#     while  i <= right:
#         if arr[i] < arr[pivot]:
#             swap(arr, i, index)
#             index+=1
#         i+=1
#     swap(arr,pivot,index-1)
#     return index-1
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]



if __name__ == '__main__':
    # numOfNum = [10,100,1000,100000]
    numOfNum = [10000]
    mode = 'quick'
    print("排序算法:"+mode)
    for each in numOfNum:
        num = generateNum(each)
        # num = [-74, -32, 7, -7, 8, 15, 23, 58, 87, 96]
        start = time.time()
        if(mode == 'bubble'):
            result = bubbleSort(num)
        elif(mode == "selection"):
            result = selectionnSort(num)
        elif(mode == 'insertion'):
            result = insertionSort(num)
        elif(mode == "quick"):
            result = quickSort(num,0,len(num)-1)
            # result = quickSort(num)
        end = time.time()
        print("程序输入：",num)
        print("程序输出：",result)
        print("运行时间：",end-start,"s")
