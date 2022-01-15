class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        #An easy way to Rotate a matrix once by 90 degrees clockwise, 
        #is to get the transpose of a matrix ( an operator which flips a matrix over its diagonal), then
        #interchange the 'j'th and 'n-1-j'th column, for 0<=j<=n-1 where n is the number of columns in matrix.
        for i in range(4):
            if mat==target:return True
            mat=[list(i) for i in list(zip(*mat[::-1]))]
            print(mat)
        return False
            
                
        
        