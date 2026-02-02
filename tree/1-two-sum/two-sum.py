class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mapp = defaultdict()
        for i, num in enumerate(nums):
            print(i, num)
            alternate = target - num
            if alternate in mapp.keys():
                return [mapp[alternate],i]
            mapp[num] = i 
