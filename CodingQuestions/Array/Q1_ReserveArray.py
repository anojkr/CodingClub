class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
            Time Complexity: O(N)
            Auxiliary Space: O(1)
        """
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
