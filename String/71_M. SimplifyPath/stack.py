class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        newpath = path.split("/")
        stack = []
        for c in newpath:
            if c == "..":
                if stack:
                    stack.pop()
            elif c != '' and c != '.':
                stack.append(c)
            

        return "/" + "/".join(stack)
