class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        b=[]
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        print(a)
        d=sorted(a.items(), key=lambda x:x[1], reverse=True)
        print(d)
        for i in range(k):
            b.append(d[i][0])
        return b