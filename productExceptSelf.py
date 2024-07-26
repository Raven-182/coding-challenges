# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = 1
    suffix = 1
    answers = [0]*n
    for i in range(n):
        answers[i] = prefix
        prefix = prefix * nums[i]
    for j in range(n-1, -1, -1):
        answers[j] *= suffix
        suffix *= nums[j]

    return answers
