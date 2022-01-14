class Solution:
    def intToRoman(self, num: int) -> str:
        dic={1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",} 
        #I, VX
        #X, LC
        #C, DM
        res=""
        nums=sorted(dic.keys(),reverse=True)
        
        for i in range(0,len(nums),2):
            cur=num//nums[i]
            num=num%nums[i]
            if 0<cur<4:res+=dic[nums[i]]*cur
            elif i>0 and cur==4:res+=dic[nums[i]]+dic[nums[i-1]]
            elif i>0 and 5<=cur<9:res+=dic[nums[i-1]]+dic[nums[i]]*(cur-5)
            elif i>0 and cur==9:res+=dic[nums[i]]+dic[nums[i-2]]
        return res
            
            
                