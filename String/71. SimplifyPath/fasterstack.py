class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        words = path.split("/")
        stack = []
        for word in words:
            if word == ".":
                continue
            elif word == "":
                continue
            elif word == "..":
                if stack: 
                    last_dir = stack.pop()
            else:
                stack.append(word)
            
        return  "/" + "/".join(stack)
