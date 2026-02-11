class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if n-k ==0:
            return sum(cardPoints)
        
        left_sum = sum(cardPoints[:k])
        right_sum =0
        total_sum =left_sum+right_sum

        for i in range(1,k+1):
            left_sum -= cardPoints[k-i]
            right_sum += cardPoints[-i]
            total_sum = max(total_sum, left_sum+right_sum)

        return total_sum



        