class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        a=[]
        res=[0]*len(nums)
        for i, e in enumerate(nums):
            while a and nums[a[-1]]<e:
                b=a.pop()
                res[b]=i-b
            a.append(i)
        return res