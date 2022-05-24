class Solution:
    def kWeakestRows(self, mat, k):
        
        m = len(mat)
        
        soldiers = []
        for row in range(m):
            soldiers.append(sum(mat[row]))


        unique_soldiers = list(set(soldiers))

        weakest = []
        for i in unique_soldiers:
            index = 0
            for j in range(soldiers.count(i)):
                index = soldiers.index(i,index)
                weakest.append(index)
                index += 1
                
        return weakest[:k]
