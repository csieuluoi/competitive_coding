"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""
# O(N)
# use a stack to keep track of the close parentheses
# loop through all characters->O(N)
# check if it is a close parenthese
# if True,
#    check if it's open parenthese type in the top of stack,
#       if True, pop that close parenthese out
#       otherwise, return False, because this close parenthese does not have its open parenthese
# if False,
#    skip and add the next character to the stack
# when finish the loop
# check if length of the stack == 0,
#    if it is, return True
#    otherwise, return False
def isValid(s: str) -> bool:
        pairs = {
                ")":"(",
                "]":"[",
                "}":"{"
            }
        stack = []

        for c in s:

            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) > 0 and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

if __name__ == "__main__":

    # this should print True
    print(isValid("()()(){}[][]([{[]}])"))
