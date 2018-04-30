class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 1
        left, right = 0, len(s) - 1
        while left < right:
            print(s[left], s[right], left, right)
            if s[left] != s[right]:
                print("hey")
                if count == 0:
                    return False
                elif s[left + 1] == s[right]:
                    count -= 1
                    left += 1
                    continue
                elif s[left] == s[right - 1]:
                    count -= 1
                    right -= 1
                    continue
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True
if __name__ == '__main__':
    a = Solution()
    print(
        a.validPalindrome(
            "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupculmgmqfvnbgtapekouga"
        )
    )
