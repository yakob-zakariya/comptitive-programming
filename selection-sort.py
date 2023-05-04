#User function Template for python3

class Solution:
    def select(self,arr,i):
        #code here
        min_index = i
        for j in range(i +1 ,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            self.select(arr,i)
        return arr
