class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr=[gas[i]-cost[i] for i in range(len(gas))]
        ts=0
        start=0
        #print(arr)
        for i,v in enumerate(arr):
            
            if v>=0 and ts==0:
                
                start=i
                ts+=v
                continue
            if ts>0:
                ts+=v
            if ts<0:
                ts=0
            #print(i,ts)
            
            
        return start if sum(arr)>=0 else -1
        """
        [2,3,4]
        [3,4,3]
        [5,1,2,3,4]
        [4,4,1,5,1]"""        
        