class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k =1
        left = 0
        max_sum = 0
        zero_cnt = 0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_cnt +=1
            if zero_cnt>k:
                if nums[left] ==0:
                    zero_cnt-=1
                left+=1
        print(right)
        print(left)
        print(max(zero_cnt,1))
        return right - left