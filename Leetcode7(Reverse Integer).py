class Solution:
    def reverse(self, x: int) -> int:
        total=0
        sign = True #set a boolen to check if the number is negative
        if x>0:
            sign = True
        else:
            sign = False
        x=abs(x)
        while(x>0):
            total=total*10 + x%10   #formula, to reverse a number
            x=x//10
        if total in range(-2**31, 2**31-1):
            if sign == True:
                return total
            else:
                return -total   #return number with '-'
        else:
            return 0
