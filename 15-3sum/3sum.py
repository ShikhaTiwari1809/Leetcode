class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        

        for i in range(len(nums)):
            low = i+1
            high = len(nums)-1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while low < high:
                summ = nums[low] + nums[high] + nums[i]
                if summ == 0:
                    triplets.append([nums[i], nums[low],nums[high]])
                    low+=1
                    high-=1
                    
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                
                elif summ < 0:
                    low+=1
                
                else:
                    high-=1
            

        return triplets