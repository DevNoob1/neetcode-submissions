class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        c=0
        for i in numbers:
            c=target-i
            if c in numbers:
                return ([numbers.index(i)+1,numbers.index(c)+1])
                break
        