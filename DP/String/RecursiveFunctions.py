"""
####### Longest common subsequence #######
        Given:
            stringA
            stringB

        if stringA[i] == stringB[j]:
            return 1+longestCommonSubsequence(stringA, stringB, i-1, j-1)
        else:
            return max(longestCommonSubsequence(stringA, stringB, i, j-1), longestCommonSubsequence(stringA, stringB, i-1, j))
"""

"""
####### Longest common substring #######
        Given:
            stringA
            stringB

        if stringA[i] == stringB[j]:
            return 1+longestCommonSubsequence(stringA, stringB, i-1, j-1)
        else:
            return 0
"""

"""
####### Shortest common super-sequence #######
    Given:
        stringA
        stringB
    Answer = len(stringA)+len(stringB)-longestCommonSubsequence(stringA, stringB, len(stringA), len(stringB))
"""

"""
####### Longest Palindromic subsequence #######
    Given : strPattern
    
    stringA = strPattern
    stringB = strPattern.reverse()
    Answer = longestCommonSubsequence(stringA, stringB, len(stringA), len(stringB))

"""

"""
####### MinimumNumberOfDeletionToMakeStringPalindrome ##########
    Given : strPattern
    
    stringA = strPattern
    stringB = strPattern.reverse()
    Answer = len(stringA) - longestCommonSubsequence(stringA, stringB, len(stringA), len(stringB))
"""

"""
####### MinimumNumberOfInsertionToMakeStringPalindrome ##########
    Given : strPattern
    
    stringA = strPattern
    stringB = strPattern.reverse()
    Answer = len(stringA) - longestCommonSubsequence(stringA, stringB, len(stringA), len(stringB))
"""

"""
####### Largest Repeating Subsequence #######

    #Recursion Function
    stringOne = string
    stringTwo = string.reverse()
    
    def solve(stringOne, stringTwo, i, j):
        if stringOne[i] == stringTwo[j] and  i!=j:
            return 1 + solve(stringOne, stringTwo, i-1, j-1)
        else:
            return max(solve(stringOne, stringTwo, i, j-1),  solve(stringOne, stringTwo, i-1, j))
"""