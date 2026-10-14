class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix)-1

        while(lr <= rr):
            mr = (lr + rr)//2
            if(matrix[mr][-1] < target):
                lr = mr+1
            elif(matrix[mr][0] > target):
                rr = mr-1
            else: break

        if(lr > rr): return False
        row = (lr + rr)//2
        lc, rc = 0, len(matrix[0])-1

        while(lc <= rc):
            mc = (lc + rc)//2
            if(matrix[row][mc] < target):
                lc = mc+1
            elif(matrix[row][mc] > target):
                rc = mc-1
            else: break
        col = (lc +rc) //2
        if(lc > rc): return False
        return True

