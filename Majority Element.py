class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        i = 0
        while i < len(nums):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
            i += 1
        result = max(hashmap, key=hashmap.get)
        return result
        
