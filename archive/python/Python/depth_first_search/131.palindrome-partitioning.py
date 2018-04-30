class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def get_is_valid(s):
            n = len(s)
            # 2D array whether start, end index substring is palindrome or
            # not
            is_palindrome = [
                [False for i in range(len(s))] for i in range(len(s))]
            for i in range(n):
                if i != n - 1:
                    is_palindrome[i][i + 1] = (s[i] == s[i + 1])
                is_palindrome[i][i] = True

        #     print(is_palindrome)
            for i in range(n - 3, -1, -1):
                for j in range(i + 2, n, 1):
                    is_palindrome[i][j] = (
                        is_palindrome[i + 1][j - 1] and s[i] == s[j])
            return is_palindrome
        result = []
        if not s or len(s) == 0:
            return result
        is_palindrome = get_is_valid(s)
        partition = []
        self.dfs(partition, s, 0, result, is_palindrome)
        return result

        is_palindrome = get_is_valid(s)

    def dfs(self, partition, s, start_index, result, is_palindrome):
        if (start_index == len(s)):
            result.append(self.get_string(partition, s))
            return

        for i in range(start_index, len(s)):
            if not is_palindrome[start_index][i]:
                continue
            partition.append(i)
            self.dfs(partition, s, i + 1, result, is_palindrome)
            partition.pop()

    def get_string(self, partition, s):
        result = []
        start_index = 0
        for i in range(len(partition)):
            result.append(s[start_index:partition[i] + 1])
            start_index = partition[i] + 1
        return result
