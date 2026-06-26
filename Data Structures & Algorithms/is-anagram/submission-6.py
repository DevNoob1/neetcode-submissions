class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
        # a=sorted(set(s))
        # b=sorted(set(t))
        # c=0
        # if len(a)!=len(b):
        #     return False
        # else:
        #     print(a,b)
        #     for i in range(len(a)):
        #         print(a[i],b[i])
        #         if a[i] in b:
        #             c=1
        #         else:
        #             c=0
        #             break;
        # return bool(c)
        # # if the two words have same character so
        # # their set length will be same
        # # if not then its false
        # # if lenght is same
        # # they might have same char might now
        # # but we got to check if they have same characters
        # # so if same lenght, 
        # # like
        # # {a,v,c}
        # # {a,b,c}
        # # we pass throught each dict
        # # for loop
        # # if a in s,t:
        # #     true
        # # else:
        # #     false break