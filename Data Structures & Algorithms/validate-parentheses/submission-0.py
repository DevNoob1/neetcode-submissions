class Solution:
    def isValid(self, s: str) -> bool:
        d={"[":"]","{":"}","(":")"}
        a=[]
        for i in s:
            if i in d:
                a.append(i)
            else:
                if not a:
                    return False
                top=a.pop()
                if d[top]!=i:
                    return False
        return not a