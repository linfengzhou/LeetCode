# my solution
class Solution(object):

    def lengthOfLastWord(self, s):
        s_list = s.strip().split(' ')
        return len(s_list[-1])
