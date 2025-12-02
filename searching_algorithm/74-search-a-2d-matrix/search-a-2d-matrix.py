class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        last_col = len(matrix[0])
        last_row =len(matrix)
        correct_row =0
        
        while correct_row!=last_row:
            if target>matrix[correct_row][last_col-1]:
                correct_row+=1
            else:
                break
        if target > matrix[last_row-1][last_col-1]:
            return False
        nums = matrix[correct_row]
        
        l =0
        r = len(nums)-1
        while l<=r:
            m= (l+r)//2
            if nums[m]==target:
                return True
            elif target< nums[m]:
                r=m-1
            else:
                l=m+1
        return False



        