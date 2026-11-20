class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap
        difference = {} # differences to indices

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in difference:
                return [difference[nums[i]], i]
            else:
                difference[diff] = i