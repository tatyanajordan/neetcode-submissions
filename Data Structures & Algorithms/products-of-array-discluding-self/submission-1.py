class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create result list filled with 0s
        # Example: [1, 2, 4, 6] → [0, 0, 0, 0]
        res = [0] * len(nums)

        # PASS 1: Calculate the product of numbers to the LEFT
        prefix = 1  # Running product of numbers we've already visited

        for i in range(len(nums)):  # Visit each index from left to right
            res[i] = prefix   # Store the product of numbers BEFORE index i
            prefix *= nums[i] # Include current number for the NEXT index

        # PASS 2: Calculate the product of numbers to the RIGHT
        postfix = 1  # Running product of numbers we've already visited from the right

        # Start at the last index and move backward to index 0
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix  # Multiply left product by right product
            postfix *= nums[i] # Include current number for the NEXT index

        return res  # Return the completed answer