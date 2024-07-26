# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

def maxOperations(nums: list[int], k: int) -> int:
    #need to find how many pairs of elements make k, but cant use the same index in more than one successful target sum
    nums.sort()
    right, left = len(nums) - 1, 0
    operations = 0
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == k:
            operations += 1
            left += 1 
            right -= 1
        #assuming that list is ascending? Better to sort
        elif (sum < k ):
            #need a bigger value
            left += 1
        else:
            right -= 1
