# Hash Map
class Solution:
    def twoSum(self, nums, target: int):
        
        hm = {}
        for i in range(0,len(nums)):
            # print(hm)
            if(target-nums[i] in hm):
                return [i,hm[target-nums[i]]]
            hm[nums[i]] = i

s = Solution()
sol = s.twoSum([1,5,3,2,4],6)
print(sol)