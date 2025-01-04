#Brute Force:​
class Solution:​
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead.​"""​
        temp=[]​
        for i in range(len(nums)):​
            if nums[i]!=0:​
                temp.append(nums[i])​
        for i in range(len(temp)):​
            nums[i]=temp[i]​
        for i in range(len(nums)-len(temp)):​
            nums.pop(len(temp)+i)​
            nums.insert(len(temp)+i,0)​
        
#Better:​
class Solution: 
 def pushZerosToEnd(self, arr): ​
 # Position to place the next non-zero element ​
 pos = 0 ​
 n = len(arr) ​
 # Move non-zero elements forward ​
 for i in range(n): ​
  if arr[i] != 0: ​
   arr[pos] = arr[i] ​
   pos += 1 ​
 # Fill the rest of the array with zeros ​
 while pos < n: ​
  arr[pos] = 0 ​
  pos += 1 ​
 return arr ​