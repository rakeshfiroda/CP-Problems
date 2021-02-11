class Solution:
    def middle(self,A,B,C):
        return (A+B+C)-(min(A,B,C)+max(A,B,C))
