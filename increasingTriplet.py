class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = None
        for n in nums:
            if first is None or n <= first:
                first = n
            elif second is None or n <= second:
                second = n
            else:
                return True
        return False