class Solution:
    def numberToWords(self, num: int) -> str:
        switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
        switcher2 = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
        switcher3 = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
        def helper(num):
            rt=""
            hd=num//100
            if hd>0:rt+=switcher[hd]+" Hundred"
            tens=(num%100)//10
            if tens==1:
                left=num%100
                if left>0:
                    carry=rt+" " if rt else ""
                    rt=carry+switcher2[left]
            elif tens>1:
                carry=rt+" " if rt else ""
                rt=carry+switcher3[tens]
                ones=num%10
                if ones>0:
                    carry=rt+" " if rt else ""
                    rt=carry+switcher[ones]
            elif tens==0:
                ones=num%10
                if ones>0:
                    carry=rt+" " if rt else ""
                    rt=carry+switcher[ones]
            return rt
            
                
            
        
        #print(2**31-1) 2147483647
        def parser(num):
            res=""
            bl=num//(10**9)
            if bl>0:res+=switcher[bl]+" Billion"
            ml=(num%(10**9))//(10**6)
            if ml>0:
                carry=res+" " if res else ""
                res=carry+ helper(ml)+" Million"
            th=(num%(10**6))//(10**3)
            if th>0:
                carry=res+" " if res else ""
                res=carry+ helper(th)+" Thousand"
            left=num%1000
            if left>0:
                carry=res+" " if res else ""
                res=carry+ helper(left)
            return res
        if num==0:return "Zero"
        return parser(num)
        
        
            
        
            