class Solution:
    def isValid(self, s: str) -> bool:
        a={"(":")","[":"]","{":"}"}
        stack=[]
        for i in s:
            if i in a:
                stack.append(i)
            else:
                if not stack:
                    return False
                t=stack.pop()
                if a[t]!=i:
                    return False
        return not stack