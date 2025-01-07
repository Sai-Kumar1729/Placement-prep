#BF approach​
# User function Template for python3 ​

class Solution: ​

def lenOfLongestSubarr(self, arr, k): ​

length=0​

        for i in range(len(arr)):​

            sum=0​

            for j in range(i, len(arr)):​

                sum+=arr[j]​

                if sum==k:​

                    length=max(length, j-i+1)​

        return length​

#Optimal Solution​

​

# User function Template for python3 ​

class Solution: ​

def lenOfLongestSubarr(self, arr, k): ​

# code here ​

index_map={} ​

index_map[0]=-1 ​

curr_sum=0 ​

length=0 ​

for i in range(len(arr)): ​

 curr_sum+=arr[i] ​

if curr_sum-k in index_map: ​

 length=max(length, i-index_map[curr_sum-k]) ​

if curr_sum not in index_map: ​

 index_map[curr_sum]=i ​

return length​
