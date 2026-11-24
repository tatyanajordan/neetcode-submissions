# wrong

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#        result = 0
#        seen = set() # thought process was to clean duplicates 
#        for i, n in enumerate(nums): 
#             if n not in seen:
#                 seen.add(n)
#             continue # when all dupes were cleaned the next thought was to increment the result by one if the value of the current iteration  that the loop was currently on had a number in the list that was larger than it in sequential order.
#        while nums[n] < max(nums):
#             result += 1
#             break

#        return result


# actually runs , but inefficient
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#        result = 0

#        for n in nums:
#         if n + 1 in nums:
#            result += 1
#         continue

#        return result


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:        # n is the start of a run
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest