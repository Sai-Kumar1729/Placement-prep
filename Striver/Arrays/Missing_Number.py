class Solution:​

    def missingNumber(self, nums: List[int]) -> int:​

        n=len(nums)​

        sum_nums=n*(n+1)/2​

        return round(sum_nums-sum(nums))​
