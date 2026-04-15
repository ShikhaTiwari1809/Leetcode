class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i in range(len(nums)):
            if nums[i] in seen.keys():
                return [i, seen[nums[i]]]
            
            seen[target - nums[i]]=i
            