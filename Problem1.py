class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:

                        if nums[i] == nums[j]:
                            indices = [ nums.index(nums[i]), nums.index(nums[j], nums.index(nums[i]) + 1 ) ] 
                        else:
                            indices = [ nums.index(nums[i]), nums.index(nums[j]) ] 
        
        
                        return indices
