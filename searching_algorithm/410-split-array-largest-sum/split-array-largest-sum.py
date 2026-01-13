class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        low, high = max(nums), sum(nums)
        
        def can_split(mid):
            part = 1
            cum_sum =0

            for i in nums:
                if cum_sum+i <= mid:
                    cum_sum += i
                else:
                    part+=1
                    cum_sum = i
                    if part>k:
                        return False
            return True
        
        while low<=high:
            mid = (low+high)//2

            if can_split(mid):
                high = mid -1
            else: 
                low = mid+1
        return low

        