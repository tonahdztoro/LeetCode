class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        reduced = num
        steps = 0
        
        while True:
            if reduced%2 == 0 and reduced != 0:
                reduced = reduced/2
                steps += 1
            elif reduced%2 != 0 and reduced != 0:
                reduced -= 1
                steps += 1
            else:
                break
                
        return steps
