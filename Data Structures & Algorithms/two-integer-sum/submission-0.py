class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        placeholder = {}
        # [0, 1, 2 , 3] - indexes - i
        # [1, 2, 3 , 4] - values - j
        # target is 7
        for i, num in enumerate(nums):
            # 7 - 1
            # I need indexes 2 and 3 to produce 3 + 4 which = 7
            
            complement = target - num
            if complement in placeholder:
                return [placeholder[complement], i]
            
            placeholder[num] = i

        return []
    





