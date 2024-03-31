class Solution(object):
    def plusOne(self, digits):
        a = len(digits) - 1
        while a >= 0:
            if(digits[a] == 9):
                digits[a] = 0
            else:
                digits[a] += 1
                return digits
            a -= 1

        return [1] + digits