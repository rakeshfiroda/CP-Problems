class Solution:
    def findDuplicate(self, nums):
        hash_map = {}
        for index,value in enumerate(nums):
            if value in hash_map.values():
                return value
            else:
                hash_map[index] = value
