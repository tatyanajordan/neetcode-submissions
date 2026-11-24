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