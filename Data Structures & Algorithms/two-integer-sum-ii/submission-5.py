class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            d=target-i
            if d in numbers and d!=i:
                return [numbers.index(i)+1, numbers.index(d)+1]
        return