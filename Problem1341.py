class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        number = num
        while number != 0:
            if number%2 == 0:
                number /= 2
            else:
                number -= 1
            steps += 1
        return steps
