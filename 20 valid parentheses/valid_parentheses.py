class Solution:
    def find_matching(self, string, parentheses_dict, parenthesis_dict_backward):
        garbage =''
        string_copy = string
        dictionary_of_truth = {}
        if string[-1] in parentheses_dict:
            return False

        if len(string) > 3:
            if string[-2] in parentheses_dict and string[-3] in parentheses_dict:
                return False
        if string[-2] in parentheses_dict:
            if parentheses_dict[string[-2]] != string[-1]:
                return False
        for char in string:
            if not char in dictionary_of_truth:
                dictionary_of_truth[char] = 1
            else:
                dictionary_of_truth[char] += 1
        
        if "[" in dictionary_of_truth:
            if "]" in dictionary_of_truth:
                if (dictionary_of_truth["["]!= dictionary_of_truth["]"]):
                    return False
            else:
                return False

        if "{" in dictionary_of_truth:
            if "}" in dictionary_of_truth:
                if (dictionary_of_truth["{"]!= dictionary_of_truth["}"]):
                    return False
            else:
                return False
        
        if "(" in dictionary_of_truth:
            if ")" in dictionary_of_truth:
                if (dictionary_of_truth["("]!= dictionary_of_truth[")"]):
                    return False
            else:
                return False
        
        
        i= 0
        while i < len(string_copy):
            if string_copy[i] in parenthesis_dict_backward and len(garbage) ==0:
                break
            elif string_copy[i] in parentheses_dict and string_copy[i+1] in parenthesis_dict_backward and parentheses_dict[string_copy[i]]!= string_copy[i+1]:
                break

            if parentheses_dict[string_copy[i]] == string_copy[i+1]:
                garbage+=string_copy[i:i+2]
                string_copy = string_copy[:i]+string_copy[i+2:]
                i = 0
            elif parentheses_dict[string_copy[i]] != string_copy[i+1] and i+1 == len(string) -1:
                break
            else:
                i += 1

        if len(garbage) == len(string):
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        
        parentheses_dict = {
            "(":")",
            "{":"}",
            "[":"]",
        }

        parentheses_dict_backwards = {
            ")": "(",
            "}":"{",
            "]":"["
        }
        

        possible_chars = ["(",")",
            "{","}",
            "[","]"]

        if len(s) % 2 !=0 :
            return False
        
        if len(s) == 2 and s[0] in parentheses_dict_backwards:
            return False
        
        if s[0] in parentheses_dict_backwards or s[-1] in parentheses_dict:
            return False
        
        for char in s:
            if not char in possible_chars:
                return False
        
        return self.find_matching(s, parentheses_dict, parentheses_dict_backwards)



a = Solution()
print(a.isValid("()")) #true
print(a.isValid("()[]{}")) #true
print(a.isValid("(]"))# false
print(a.isValid("[()]")) # true
print(a.isValid("["))#false
print(a.isValid("(){}}{"))#false
print(a.isValid("(}{)"))#false
print(a.isValid("]["))#false
print(a.isValid("(([]){})"))#true
print(a.isValid("({[)"))#false
print(a.isValid("[[[]"))#false
print(a.isValid("[({(())}[()])]"))#true
print(a.isValid("([)]"))#false
print(a.isValid("({{{{}}}))"))#false
print(a.isValid("[([]])"))#false
# print(find_matching("[({(())}[()])]", parentheses_dict))
