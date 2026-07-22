class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        for c in s: #for each character in the string
            if c in hashmap: #if the character is a closing bracket
                if stack and stack[-1] == hashmap[c]: #if there is something in stack, and the top of the stack is == to the value of the index of the current hashmap
                    stack.pop() #pop from the array
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
