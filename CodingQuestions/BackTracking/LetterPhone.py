class Solution:
    # @param A : string
    # @return a list of strings
    def getPermute(self, start, N, A, hash_dict, arr, result):
        if start == N:
            result.append("".join(map(str,arr)))
            return
        nums = hash_dict.get(A[start])
        for ele in nums:
            arr.append(ele)
            self.getPermute(start + 1, N, A, hash_dict, arr, result)
            arr.pop()

    def letterCombinations(self, A):
        hash_dict = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        arr = []
        self.getPermute(0, len(A), A, hash_dict, arr, result)
        return result
