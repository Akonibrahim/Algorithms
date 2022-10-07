class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = set(')]}')
        opening = set('([{')
        pair = {')' : '(' , ']' : '[' , '}' : '{'}
        for i in s:
            if i in opening:
                stack.append(i)
            if i in closing:
                if not stack :
                    return False
                if stack.pop() != pair[i] :
                    return False
        if stack:
            return False
        
        return True


s = Solution()
print(s.isValid("{[]}"))