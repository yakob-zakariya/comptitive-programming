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
    
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            self.select(arr,i)
        return arr
my_solution = Solution()
arr = [10,2,3,-4,0]

print(my_solution.selectionSort(arr))
