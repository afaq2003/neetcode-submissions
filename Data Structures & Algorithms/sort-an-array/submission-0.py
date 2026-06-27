class Solution(object):
    def sortArray(self, nums):
        def merge(arr,L,M,R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            k=L
            i=0
            j=0
            temp = []
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1

        def merge_sort(arr,l,r):
            if l==r:
                return arr 
            m = (l+r)//2
            merge_sort(arr,l,m)    
            merge_sort(arr,m+1,r)
            merge(arr,l,m,r) 
            return arr
        return merge_sort(nums,0,len(nums)-1)
        
       



                
        