class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l =0
        n=len(nums)
        r=n-1

        while l<=r:
            mid = (l+r)//2
            print(mid)
            if nums[mid]==target:
                start = mid
                end = mid
                while end+1<n and nums[end+1]==target: 
                    end = end+1
                while start-1 >=0 and nums[start-1]==target:
                    start = start-1
                return [start,end]
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        
        return[-1,-1]