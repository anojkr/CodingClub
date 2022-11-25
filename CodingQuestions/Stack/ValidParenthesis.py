"""
Follow the steps mentioned below to implement the idea:
    1.  Declare a character stack (say temp).
    2. Now traverse the string exp.
    3. If the current character is a starting bracket ( ‘(‘ or ‘{‘  or ‘[‘ ) then push it to stack.
    4. If the current character is a closing bracket ( ‘)’ or ‘}’ or ‘]’ ) then pop from stack and if the popped character is the matching starting bracket then fine.
       Else brackets are Not Balanced.
    5. After complete traversal, if there is some starting bracket left in stack then Not balanced, else Balanced.
"""
class Solution:
    def isValid(self, s: str) -> bool:

        Stack = []
        HashMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for ele in s:
            if len(Stack) > 0:
                if HashMap.get(ele) == Stack[-1]:
                    Stack.pop()
                else:
                    Stack.append(ele)
            else:
                Stack.append(ele)
        return len(Stack) == 0
