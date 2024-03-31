class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        str_array = s.split()

        return len(str_array[-1])   