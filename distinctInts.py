class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 ={nums1}
        set2 = {nums2}
        answer =[[],[]]
        for num in set1:
            if num not in set2:
                answer[0].append(num)
        for num in set2:
            if num not in set1:
                answer[1].append(num)    
        return answer