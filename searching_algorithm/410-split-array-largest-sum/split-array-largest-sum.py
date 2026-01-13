class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        low, high = max(nums), sum(nums)

        def can_split(max_allowed: int) -> bool:
            parts = 1
            curr_sum = 0
            for x in nums:
                if curr_sum + x <= max_allowed:
                    curr_sum += x
                else:
                    parts += 1
                    curr_sum = x
                    if parts > k:
                        return False
            return True

        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1

        return low