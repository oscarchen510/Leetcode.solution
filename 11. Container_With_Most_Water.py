'''由左右往中間檢查，左邊比較小就加左邊的數，反之亦然'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while r>l:
            area = (r-l)*min(height[l],height[r]) #計算面積
            res = max(res,area) #取最大
            if height[l]<height[r]:
                l += 1
            else: #相等也會繼續檢查，不然跳不出迴圈
                r-=1
        return res
