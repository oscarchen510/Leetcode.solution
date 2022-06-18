import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.search(p,s) #re套件用來表達regular expression，re.search(pattern,string)就是regular expression的 string 然後跟 pattern配對比較，而re.search會匹配整个字符串，直到找到一个匹配。沒有回傳None
        if res is None:
            return False
        grp = res.group() #group()會回傳re.search(p,s)的所有東西，上面已配對好
        if(s == grp):
            return True
        else:
            False
