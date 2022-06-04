class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""    #set empty array
        resLen = 0  #set initial value to control the longest array length
        for i in range(len(s)):
            #odd length
            l,r = i,i   #從最左邊開始找，i為中心，左右延伸去找
            while l>=0 and r<len(s) and s[l]==s[r]:#s[l]==s[r]超重要!!!
                if (r-l+1)>resLen:  #record longest array length
                    res = s[l:r+1]  #record longest array
                    resLen = r-l+1
                l-=1    #find string on left side 
                r+=1    #find string on right side 
            #even length
            l,r = i,i+1 #even number don't have center number, so just +1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return 
