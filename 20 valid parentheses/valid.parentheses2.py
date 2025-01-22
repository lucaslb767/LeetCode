class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        stack_for_opening = []
        for char in s:
            if char in parentheses_dict:
                stack_for_opening.append(char)
            else:
                if len(stack_for_opening) == 0 or parentheses_dict[stack_for_opening.pop()] != char:
                    return False
        return True if len(stack_for_opening) ==0 else False