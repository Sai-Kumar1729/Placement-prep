#BF​

class Solution:​

    def majorityElement(self, nums: List[int]) -> int:​

        n=len(nums)​

        for i in range(n):​

            count=0​

            for j in range(n):​

                if nums[i]==nums[j]:​

                    count+=1​

            if count>n/2:​

                return nums[i]​
#Better​
​
class Solution:​

    def majorityElement(self, nums: List[int]) -> int:​

        n=len(nums)​

        hash_count={}​

        for i in nums:​

            if i in hash_count:​

                hash_count[i]+=1​

            else:​

                hash_count[i]=1​

            if hash_count[i]>n//2:​

                return i​

​

​
​

​
