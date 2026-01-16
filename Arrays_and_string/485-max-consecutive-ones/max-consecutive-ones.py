class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        current_cnt = 0
        for i in nums:
            
            if i == 1:
                current_cnt+=1
            else:
                current_cnt = 0
            cnt = max(current_cnt,cnt)
        
        return cnt